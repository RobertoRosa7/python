# -*- coding: utf-8 -*-
import os, sys, json
import re
import asyncio

sys.path.append(os.path.abspath(os.getcwd()))

from flask import jsonify, request, Blueprint
from bson.json_util import dumps, ObjectId
from api_server.enviroment.enviroment import get_collection, db
from api_server.robots.get_status_code import get_status_code


dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")

def calcular_consolidado(lists):
  consolidado = {
    "total_credit": 0,
    "total_debit": 0,
    "total_consolidado": 0
  }

  for i in range(len(lists)):
    if lists[i]['type'] == 'incoming':
        consolidado['total_credit'] += float(lists[i]['value'])
    elif lists[i]['type'] == 'outcoming':
        consolidado['total_debit'] += float(lists[i]['value'])

  consolidado['total_consolidado'] += (consolidado['total_credit'] - consolidado['total_debit'])
  return consolidado

@dashboard.route("/fetch_registers", methods=["GET"])
def fetch_registers():
  try:
    data = {'results': [] }

    result = get_collection('collection_registers').find()

    dumps_result = dumps(result)
    str_to_json = json.loads(dumps_result)
    
    data['consolidado'] = calcular_consolidado(str_to_json)

    for i in range(len(str_to_json)):
        data['results'].append(str_to_json[i])

    response = jsonify({'status':200, 'msg': 'total de registros: ' + str(len(str_to_json)), 'data': data})
    response.status_code = 200
    return response
  except Exception as e:
    return not_found(e)


@dashboard.route("/new_register", methods=["POST"])
def new_register():
  try:
    payload = request.json
    payload['status'] = 'done'
    get_collection('collection_registers').insert(payload)
    response = jsonify({'status':200, 'msg': 'Registro adicionado'})
    response.status_code = 200
    
    return response
  except Exception as e:
   return not_found(e)


@dashboard.route("/calc_consolidado", methods=["GET"])
def calc_consolidado():
  payload = {
      "total_credit": 0,
      "total_debit": 0,
      "total_consolidado": 0
    }
  try:
    result = get_collection('collection_registers').find()
    response = dumps(result)
    data = json.loads(response)

    for i in range(len(data)):
        if data[i]['type'] == 'incoming':
            payload['total_credit'] += int(data[i]['value'])
        elif data[i]['type'] == 'outcoming':
            payload['total_debit'] += int(data[i]['value'])

    payload['total_consolidado'] += (payload['total_credit'] - payload['total_debit'])
    return jsonify(payload)
  except Exception as e:
    return not_found(e)


@dashboard.route('/update_register', methods=['POST'])
def update_one():
  try:
    payload = request.get_json()
    if not payload['_id']:
        return str(json.dumps({'status':404, 'msg':"id é obrigatório"})), 404
    
    find_id = ObjectId(payload['_id']['$oid'])
    find_result = get_collection('collection_registers').find_one({"_id": find_id})

    if find_result != None and type(find_result) == dict:
        del payload['_id']
        result = get_collection('collection_registers').update_one({"_id": find_id}, {"$set": payload})
        if result.modified_count > 0:
          return str(json.dumps({'status':200, 'msg':'Um registro foi modificado'})), 200
        else:
          return str(json.dumps({'status':200, 'msg': 'Nenhum registro foi modificado.'})), 200
    else:
       return str(json.dumps({'status':404,"msg":"Registro não foi encontrado"})), 404
  except Exception as e:
    return not_found(e)


@dashboard.route('/delete_register', methods=['POST'])
def delete_one():
  try:
    data = {'results': [] }
    payload = request.get_json()

    if not payload['_id']:
        return str(json.dumps({'status':404, 'msg':"id é obrigatório"})), 404
    
    find_id = ObjectId(payload['_id']['$oid'])
    find_result = get_collection('collection_registers').find_one({"_id": find_id})

    if find_result != None and type(find_result) == dict:
        del payload['_id']
        get_collection('collection_registers').delete_one({"_id": find_id})
       
        result = get_collection('collection_registers').find()
        dumps_result = dumps(result)
        str_to_json = json.loads(dumps_result)
        
        data['consolidado'] = calcular_consolidado(str_to_json)
        
        for i in range(len(str_to_json)):
            data['results'].append(str_to_json[i])

        response = jsonify({'status':200, 'msg': 'total de registros: ' + str(len(str_to_json)), 'data': data})
        response.status_code = 200
        return response
    else:
       return str(json.dumps({'status':404,"msg":"Registro não foi encontrado"})), 404
  except Exception as e:
    return not_found(e)


@dashboard.route('/get_status_code', methods=["GET"])
def get_code():
  try:
    data = asyncio.run(get_status_code())
    return str(json.dumps(data)), 200
  except Exception as e:
    return not_found(e)


@dashboard.errorhandler(404)
def not_found(error=None):
    message = {'status': 500, 'message': 'page found' + request.url, 'error': error}
    response = jsonify(message)
    response.status_code = 500
    return response