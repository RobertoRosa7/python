import os, sys
import re
import json

sys.path.append(os.path.abspath(os.getcwd()))

from flask import Flask, jsonify, request
from flask_script import Manager, Server
from api_server.routes.home import home
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.secret_key = 'secretkey'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/primeiroapp'


mongo = PyMongo(app)
app.register_blueprint(home)


@app.route("/", methods=["GET"])
def health_check():
  return str(json.dumps({'API':"it's working"})), 200


@app.route("/busca-registros", methods=["GET"])
def busca_registro():
  try:
    result = mongo.db.collection_registers.find()
    response = dumps(result)
    return response
    # return str(json.dumps({'API':"it's working"})), 200
  except Exception as e:
    return not_found(e)


@app.route("/novo-registro", methods=["POST"])
def novo_registro():
  try:
    payload = request.json
    mongo.db.collection_registers.insert(payload)
    response = jsonify('successfully')
    response.status_code = 200
    
    return response
  except Exception as e:
   return not_found(e)


@app.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': 'page found' + request.url, 'error': error}
    response = jsonify(message)
    response.status_code = 500
    return response


if __name__ == "__main__":
  app.run(debug=True)