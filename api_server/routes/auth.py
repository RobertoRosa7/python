from flask import request
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

def get_token():
  return request.headers.get('Token', None)


def login_required(func):
  def __callback__(*args, **kwargs):
    from app.Login import g
    if not g.g_get_user():
      return '{"status":401,"message":"Usuário ou senha inválido."}', 401
    return func(*args, **kwargs)
  __callback__.__name__ = func.__name__
  return auth.login_required(__callback__)