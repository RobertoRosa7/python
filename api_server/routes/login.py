# -*- coding: utf-8 -*-
import os, sys, re, base64

from flask.globals import request

sys.path.append(os.path.abspath(os.getcwd()))

from flask import Blueprint, jsonify, render_template, make_response
from api_server.routes.auth import login_required
from api_server.utils.LoginManager import LoginManager
from api_server.enviroment.enviroment import db, API
from api_server.utils.SendEmail import SendEmail
from api_server.utils.gets import set_user, get_user
from bson.json_util import ObjectId

my_login = Blueprint("my_login", __name__, url_prefix="/login")


def valida_sufixos_hosts_email(email):
  suffixes = ['con', 'com.bt', 'combr', 'xom', 'vom', 'ckm', 'c', 'clm']
  hosts = ['gmai', 'yaho', 'outlok', 'gnail', 'hotmai', 'gmaol', 'gemail', 'outloo', 'ganil', 'gamil', 'hotnail', 'g.mail', 'gmnail', 'hotmaim', 'hotmais', 'hotmaiil', 'msm']
  splitAddress = email.split('@')
  splitAddress = splitAddress[1].split('.')
  
  if splitAddress[0] in hosts:
    return False
  else:
    addr = ('.').join(splitAddress[1:])
    if addr in suffixes:
      return False
  return True


@my_login.route('/signin', methods=['GET'])
def sign_in():
  access = request.headers.get('Authorization')

  if not access:
    return jsonify({"message": 'e-mail e senha é obrigatório'}), 400
  
  access = access.split(':')
  access_email = base64.b64decode(access[0])
  access_pass = base64.b64decode(access[1])
  
  if not access_email or not access_pass:
    return jsonify({"message": 'Campo e-mail é obrigatório'}), 400
  
  try:
    login_manager = LoginManager()
    user = db.collection_users.find_one({'email': access_email.decode('ascii')})
    check_pass = login_manager.check_password(access_pass.decode('ascii'), user['password'])
  
    if not user:
      return jsonify({"message": 'E-mail não encontrado'}), 400
    if not check_pass:
      return jsonify({"message": 'E-mail ou senha inválidos'}), 400
  
    if isinstance(user['_id'], ObjectId):
      user['_id'] = str(user['_id'])
  
    token = login_manager.generate_auth_token(user)
    set_user('user', user)
  
    return {'email': user['email'],'access_token': token.decode('ascii'),'id': str(user['_id'])}
  except Exception as e:
    return jsonify({"message": 'Error interno no servidor'}), 500


@my_login.route('/signup', methods=['POST'])
def create_user():
  data = request.get_json()
  login_manager = LoginManager()

  try:
    if 'email' not in data:
      return jsonify({"message": 'Campo e-mail é obrigatório'}), 400

    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    match = re.match(regex, data['email'].lower())

    if match is None or not valida_sufixos_hosts_email(data['email']):
      return make_response(jsonify({"message": 'Campo e-mail inválido'}), 400)

    user = {
      **data,
      'email': data['email'], 
      'password': login_manager.password_to_hash(data['password'])
      }

    user_exists = db.collection_users.find_one({'email': user['email']})
    there_is_user = user_exists if user_exists else {}

    if 'password' in there_is_user:
      return jsonify({'message': 'Usuário já cadastro', 'status': 406}), 406
    else:
      user_temp = user
      user_temp['_id'] = db.collection_users.insert_one(user).inserted_id

    user_temp['_id'] = str(user_temp['_id'])
    token = login_manager.generate_auth_token(user_temp, 600000).decode('ascii')
    template = render_template('bem-vindo.html', nome=user_temp['email'], token=token, api_url=API)
    mail = SendEmail()
    mail.send_verify_email(template, user_temp['email'])

    return jsonify({"message": 'Usuário cadastrado com sucesso'}), 201
  except Exception as e:
    return {'message': 'Error %s' % repr(e), 'status': 500}, 500


@my_login.route('/reset_password', methods=['POST'])
def reset_password():
  try:
    payload = request.get_json()

    if not payload['email']:
      return jsonify({"message": 'Campo e-mail inválido'}), 400

    login_manager = LoginManager()
    user_exists = db.collection_users.find_one({'email': payload['email']})
    
    if user_exists is not None:
      user_exists['_id'] = str(user_exists['_id'])
      token = login_manager.generate_auth_token(user_exists, 600000).decode('ascii')
      template = render_template('reset_password.html', email=payload['email'], token=token, api_url=API)
      mail = SendEmail()
      mail.send_verify_email(template, payload['email'])
     
      return {'status': 200, 'message': 'Email de recuperaçao de senha enviado.'}, 200
    else:
      return {'status': 400, 'message': 'Email invalido.'}, 400
  except Exception as e:
    return {'message': 'Error %s' % repr(e), 'status': 500}, 500  
