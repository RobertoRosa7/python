from flask import g

def get(*args, **kwargs):
  return g.get(*args, **kwargs)


def set(key, value):
  g.__setattr__(key, value)


def g_get_user():
  return g.get("user", {})


def g_get_usuario():
  return g_get_user().get("usuario", {})


def g_get_email():
  return g_get_usuario().get("email", None)


def g_get_id():
  return g_get_user().get("_id")
