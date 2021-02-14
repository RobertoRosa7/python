import os, sys
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


@app.route("/")
def health_check():
  return str(json.dumps({'API':"it's working"})), 200


if __name__ == "__main__":
  app.run(debug=True)