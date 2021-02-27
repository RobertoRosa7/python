# -*- coding: utf-8 -*-
import os, sys, json, re
import asyncio
import pymongo
import datetime
import time
import pandas as pd
import numpy as np


sys.path.append(os.path.abspath(os.getcwd()))

from datetime import date, datetime as dt
from flask import jsonify, request, Blueprint
from bson.json_util import dumps, ObjectId
from api_server.enviroment.enviroment import db
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
    days = request.args.get('days', default=7, type=int)
    todos = request.args.get('todos', default=None, type=str)
    data = {'results': [] }
    evolucao = {'days': [], 'values': []}
    rangeDates = []
    filtered = {}

    for i in range(0, days):
      rangeDates.append((datetime.date.today() - datetime.timedelta(i)).isoformat())

    if todos == None:
      filtered['created_at'] = {
        '$lte': float(time.mktime(datetime.datetime.strptime(rangeDates[0], "%Y-%m-%d").timetuple())), 
        '$gte': float(time.mktime(datetime.datetime.strptime(rangeDates[-1], "%Y-%m-%d").timetuple()))
      }
    
    result = db.collection_registers.find(filtered).sort('created_at', pymongo.DESCENDING)
    
    # print(int(time.mktime(datetime.datetime.strptime(rangeDates[0], "%Y-%m-%d").timetuple())/1e3))
    dumps_result = dumps(result)
    
    df = pd.read_json(dumps_result)
    categories = pd.DataFrame(df['category']).drop_duplicates().values

    for cat in categories:
      category_format = cat[0].lower().replace(' ', '_').replace('&', 'e').replace('á','a').replace('ã','a').replace('ç','c').replace('õ','o')
      print(category_format)

    # print(len(np.array(categories)))

    str_to_json = json.loads(dumps_result)
    data['consolidado'] = calcular_consolidado(str_to_json)
    

    for i in range(len(str_to_json)):
      # temp_id = ObjectId(str_to_json[i]['_id']['$oid'])
      # del str_to_json[i]['_id']

      # conveter timestamp javascript to string
      # date = datetime.datetime.fromtimestamp(str_to_json[i]['created_at'] / 1e3).strftime('%Y-%m-%d')
      
      # date = int(time.mktime(datetime.datetime.strptime(
        # str_to_json[i]['created_at'], "%Y-%m-%d").timetuple()))
      # db.collection_registers.update_one({"_id": temp_id}, {"$set": {'created_at': date }})

      # evolucao['days'].append(str_to_json[i]['created_at'])
      # evolucao['values'].append(str_to_json[i]['value'] / 100)
      data['results'].append(str_to_json[i])

    
    # data['evolucao'] = evolucao
    data['total'] = len(str_to_json)
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
    db.collection_registers.insert(payload)
    response = jsonify({'status':200, 'msg': 'Registro adicionado'})
    response.status_code = 200
    
    return response
  except Exception as e:
   return not_found(e)


@dashboard.route("/calc_consolidado", methods=["GET"])
def calc_consolidado():
  try:
    result = db.collection_registers.find().sort('created_at', pymongo.DESCENDING)
    dumps_result = dumps(result)
    str_to_json = json.loads(dumps_result)
    consolidado = calcular_consolidado(str_to_json)
    
    response = jsonify(consolidado)
    response.status_code = 200
    return response
  except Exception as e:
    return not_found(e)


@dashboard.route('/update_register', methods=['POST'])
def update_one():
  try:
    payload = request.get_json()
    if not payload['_id']:
        return str(json.dumps({'status':404, 'msg':"id é obrigatório"})), 404
    
    find_id = ObjectId(payload['_id']['$oid'])
    find_result = db.collection_registers.find_one({"_id": find_id})

    if find_result != None and type(find_result) == dict:
        del payload['_id']
        result = db.collection_registers.update_one({"_id": find_id}, {"$set": payload})
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
    find_result = db.collection_registers.find_one({"_id": find_id})

    if find_result != None and type(find_result) == dict:
        del payload['_id']
        db.collection_registers.delete_one({"_id": find_id})
       
        result = db.collection_registers.find()
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


def get_first_date(invs, salfer=False):
  dt_lower = time.time()
  for inv in invs:
    dt_inv = inv['created_at']
    if dt_inv < dt_lower:
        dt_lower = dt_inv
  return dt_lower


def get_last_date(invs):
  last_date = None
  for inv in invs:
    current_date = inv.get('created_at', None)
    if not current_date or current_date > time.time():
      last_date = time.time()
      break
    else:
      if last_date == None:
        last_date = current_date
      elif current_date > last_date:
        last_date = current_date
  return last_date


@dashboard.errorhandler(404)
def not_found(error=None):
    message = {'status': 500, 'message': 'page found' + request.url, 'error': error}
    response = jsonify(message)
    response.status_code = 500
    return response