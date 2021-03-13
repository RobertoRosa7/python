import os, sys
from flask import request, jsonify
from flask_httpauth import HTTPBasicAuth

sys.path.append(os.path.abspath(os.getcwd()))

from api_server.utils.gets import set_user, get_user
from api_server.utils.LoginManager import LoginManager
from api_server.enviroment.enviroment import db


auth = HTTPBasicAuth()


def get_token():
  return request.headers.get('Authorization', None)


def login_required(func):
  def __callback__(*args, **kwargs):
    if not get_user():
      return jsonify({"status":401,"message":"Usuário ou senha inválido."}), 401

    return func(*args, **kwargs)
  
  __callback__.__name__ = func.__name__
  return auth.login_required(__callback__)


def check_password(func):
  return auth.verify_password(func)


@check_password
def verify_password(username, password):
  print(username, password)
  login_manager = LoginManager()
  # token = get_token()
  
  # if token is not None:
  #   user_data = login_manager.verify_auth_token(token, db.collection_users)
  if not username or password:
    set_user('user', None)
    return True
  
  # user = db.collection_users.find_one({'email': username})
  # print(user)
  return True
