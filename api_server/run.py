import os, sys
import re
import json

sys.path.append(os.path.abspath(os.getcwd()))

from flask import Flask, jsonify, request
from flask_script import Manager, Server
from flask_pymongo import PyMongo
from bson.json_util import dumps
# from bson.objectid import ObjectId
# from werkzeug.security import check_password_hash, generate_password_hash

from api_server.routes.home import home
from api_server.routes.dashboard import dashboard


app = Flask(__name__)
# app.secret_key = 'secretkey'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/primeiroapp'


app.register_blueprint(home)
app.register_blueprint(dashboard)


@app.route("/", methods=["GET"])
def health_check():
  return str(json.dumps({'API':"it's working"})), 200


@app.after_request
def after_request(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Token,Avista-Token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    # response.headers.set('Access-Control-Allow-Credentials', 'true')
    return response


if __name__ == "__main__":
  app.run(debug=True, port=3000)