from flask import Blueprint

home2 = Blueprint("home2", __name__)


@home2.route("/home2", methods=["GET"])
def home():
    return "Hello World my first API"
