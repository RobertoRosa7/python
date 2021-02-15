import os, sys, json

sys.path.append(os.path.abspath(os.getcwd()))

from flask import jsonify, request, Blueprint
from bson.json_util import dumps

from api_server.enviroment.enviroment import get_collection

dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard.route("/fetch_registers", methods=["GET"])
def fetch_registers():
  try:
    # result = db.collection_registers.find()
    # result = db.primeiroapp.get_collection('collection_registers').find()
    result = get_collection('collection_registers').find()
    response = dumps(result)
    return response
    # col = db.collection_registers
    # print(print()
    # return str(json.dumps({'API':"it's working"})), 200
  except Exception as e:
    return not_found(e)


@dashboard.route("/new_register", methods=["POST"])
def new_register():
  try:
    payload = request.json
    # db.collection_registers.insert(payload)
    get_collection('collection_registers').insert(payload)
    response = jsonify('successfully')
    response.status_code = 200
    
    return response
  except Exception as e:
   return not_found(e)


@dashboard.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': 'page found' + request.url, 'error': error}
    response = jsonify(message)
    response.status_code = 500
    return response