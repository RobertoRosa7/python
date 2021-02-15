import os, sys, json

sys.path.append(os.path.abspath(os.getcwd()))

from flask import jsonify, request, Blueprint
from bson.json_util import dumps
from api_server.enviroment.enviroment import get_collection


dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard.route("/fetch_registers", methods=["GET"])
def fetch_registers():
  try:
    result = get_collection('collection_registers').find()
    response = dumps(result)
    return response
  except Exception as e:
    return not_found(e)


@dashboard.route("/new_register", methods=["POST"])
def new_register():
  try:
    payload = request.json
    payload['status'] = 'done'
    get_collection('collection_registers').insert(payload)
    response = jsonify('successfully')
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


@dashboard.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': 'page found' + request.url, 'error': error}
    response = jsonify(message)
    response.status_code = 500
    return response