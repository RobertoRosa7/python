
# -*- coding: utf-8 -*-
import os, sys

from flask.globals import request

sys.path.append(os.path.abspath(os.getcwd()))

from flask import Blueprint, jsonify, render_template, make_response
from api_server.routes.auth import login_required
from api_server.utils.LoginManager import LoginManager
from api_server.enviroment.enviroment import db, API
from api_server.utils.SendEmail import SendEmail


my_login = Blueprint("my_login", __name__, url_prefix="/login")


@my_login.route('/signup', methods=['POST'])
def create_user():
  data = request.get_json()
  login_manager = LoginManager()
  try:

    if 'email' not in data:
      return jsonify({"message": 'Campo e-mail é obrigatório'}), 400
    
    user = {'email': data['email'], 'password': login_manager.password_to_hash(data['password'])}
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