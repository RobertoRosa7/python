from flask import Blueprint

home = Blueprint("home", __name__)


@home.route("/")
def home():
    return "Hello World my first API"
