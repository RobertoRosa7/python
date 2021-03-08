# -*- coding: utf-8 -*-
import os, sys, json, asyncio, pymongo, datetime, time, pandas as pd

sys.path.append(os.path.abspath(os.getcwd()))

from flask import jsonify, request, Blueprint
from bson.json_util import dumps, ObjectId
from api_server.enviroment.enviroment import db, set_mode
from api_server.robots.get_status_code import get_status_code


dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")


def clear_text(text):
  text.lower().replace(' ', '_').replace('&', 'e').replace('á','a').replace('ã','a').replace('ç','c').replace('õ','o')
  return text 


def build_evocucao(tipo, lists):
  build_categories = {}
  list_dates = []
  df = pd.read_json(lists)
  df = df.drop(columns=['_id', 'position', 'description', 'user', 'edit', 'status', 'brand', 'updated_at','cat_icon', 'month'])

  if tipo == 'despesas':
    coming = df.loc[df.type == 'outcoming']
  else:
    coming = df.loc[df.type == 'incoming']

  get_dates_list = pd.DataFrame(coming['created_at']).drop_duplicates().values
  df = pd.DataFrame(coming.groupby(['created_at', 'category']).sum()['value']).unstack(fill_value=0)['value'].to_json()
  str_to_json = json.loads(df)

  for i, v in str_to_json.items():
    name = clear_text(i)
    build_categories[name] = {'values': [], 'label': ''}
    build_categories[name]['label'] = i
    for d in v.values():
      build_categories[name]['values'].append(d)

  for d in get_dates_list:
    list_dates.append(int(pd.Timestamp(d[0]).timestamp()))

  build_categories['dates'] = list_dates
  return build_categories


def calcular_consolidado(lists):
  consolidado = {}
  consolidado['total_credit'] = 0
  consolidado['total_debit'] = 0
  consolidado['total_consolidado'] = 0
  consolidado['a_pagar'] = 0
  consolidado['a_receber'] = 0

  data_now = int(time.time())

  for i in range(len(lists)):
    if lists[i]['type'] == 'incoming':
      if lists[i]['created_at'] <= data_now:
        consolidado['total_credit'] += float(lists[i]['value'])
      if lists[i]['status'] == 'pending':
          consolidado['a_receber'] += float(lists[i]['value'])
    elif lists[i]['type'] == 'outcoming':
        if lists[i]['created_at'] <= data_now:
          consolidado['total_debit'] += float(lists[i]['value'])
        if lists[i]['status'] == 'pending':
          consolidado['a_pagar'] += float(lists[i]['value'])

  consolidado['total_consolidado'] += (consolidado['total_credit'] - consolidado['total_debit'])
  return consolidado


def making_filter(days, todos):
  rangeDates = []
  filtered = {}

  for i in range(0, days):
    rangeDates.append((datetime.date.today() - datetime.timedelta(i)).isoformat())

  if todos == None:
    filtered['created_at'] = {
      '$lte': time.time(), 
      '$gte': float(time.mktime(datetime.datetime.strptime(rangeDates[-1], "%Y-%m-%d").timetuple()))
    }

  return filtered


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


@dashboard.route("/fetch_evolucao_despesas", methods=["GET"])
def fetch_evolucao_despesas():
  try:
    data = {}
    result = list(db.collection_registers.find().sort('created_at', pymongo.ASCENDING))
    data = build_evocucao('despesas', dumps(result))
    response = jsonify({'graph_evolution': data})
    response.status_code = 200

    return response
  except Exception as e:
    return not_found(e)  

@dashboard.route("/fetch_evolucao", methods=["GET"])
def fetch_evolucao():
  try:
    data = {}
    result = list(db.collection_registers.find().sort('created_at', pymongo.ASCENDING))
    data = build_evocucao('receita', dumps(result))
    response = jsonify({'graph_evolution': data})
    response.status_code = 200

    return response
  except Exception as e:
    return not_found(e)


@dashboard.route("/fetch_evolucao_detail", methods=["POST"])
def fetch_evolucao_detail():
  try:
    data = {}
    payload = request.get_json()
    if not payload['_id']:
      return str(json.dumps({'status':404, 'msg':"id é obrigatório"})), 404

    find_id = ObjectId(payload['_id']['$oid'])
    find_result = db.collection_registers.find_one({"_id": find_id})
    data = build_evocucao(dumps(find_result))
    response = jsonify({'graph_evolution': data})
    response.status_code = 200
    return response
  except Exception as e:
    return not_found(e)


@dashboard.route("/fetch_registers", methods=["GET"])
def fetch_registers():
  try:
    days = request.args.get('days', default=7, type=int)
    todos = request.args.get('todos', default=None, type=str)
    data = {'results': [] }
    result = list(db.collection_registers.find(making_filter(days, todos)).sort('created_at', pymongo.DESCENDING))
    
    if len(result) > 0:
      dumps_result = dumps(result)
      str_to_json = json.loads(dumps_result)
      data['consolidado'] = calcular_consolidado(str_to_json)

      for i in range(len(str_to_json)):
        data['results'].append(str_to_json[i])
      
      data['total'] = len(str_to_json)
    
    response = jsonify({'data': data})
    response.status_code = 200

    return response
  except Exception as e:
    return not_found(e)


@dashboard.route("/new_register", methods=["POST"])
def new_register():
  try:
    payload = request.json
    data_now = int(time.time())

    if payload['created_at'] <= data_now:
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
    data_now = int(time.time())

    if not payload['_id']:
      return str(json.dumps({'status':404, 'msg':"id é obrigatório"})), 404
    
    find_id = ObjectId(payload['_id']['$oid'])

    payload['status'] = 'done' if payload['created_at'] <= data_now else 'pending'

    find_result = db.collection_registers.find_one({"_id": find_id})
    if find_result != None and type(find_result) == dict:
      del payload['_id']
      result = db.collection_registers.update_one({"_id": find_id}, {"$set": payload})

      if result.modified_count > 0:
        data = db.collection_registers.find_one({"_id": find_id})
        response = jsonify({'status':200, 'msg':'Um registro foi modificado', 'data': json.loads(dumps(data))})
        response.status_code = 200
        return response
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
      result = list(db.collection_registers.find(making_filter(7, None)).sort('created_at', pymongo.DESCENDING))
      dumps_result = dumps(result)
      str_to_json = json.loads(dumps_result)
      data['consolidado'] = calcular_consolidado(str_to_json)

      for i in range(len(str_to_json)):
        data['results'].append(str_to_json[i])

      data['total'] = len(str_to_json)
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


@dashboard.route('/set_dev_mode', methods=['POST'])
def set_dev_mode():
  try:
    data = request.get_json()
    mode = True if data['mode'] == 'dev-mode' else False
    res = set_mode(mode)
    text = 'dev-mode' if res else 'prod-mode'

    response = jsonify({'mode': text})

    return response, 200
  except Exception as e:
    return not_found(e)


@dashboard.errorhandler(404)
def not_found(error=None):
  message = {'status': 500, 'message': 'page found' + request.url, 'error': error}
  response = jsonify(message)
  response.status_code = 500
  
  return response