# -*- coding: utf-8 -*-
import json
import os, sys

sys.path.append(os.path.abspath(os.getcwd()))

from flask import Flask

# from flask_mongoengine import MongoEngine
from flask_script import Manager, Server
from flask import Blueprint
from flask import make_response
from utils.formats import Formats

# db = MongoEngine()

app = Flask(__name__)
# app.config.from_pyfile("settings.py")

# apply overrides for test
app.config.update()

# set db
# db.init_app(app)

# import blueprints
# from home.views import home_app
# from pet.views import pet_app
# from app.pages.home import home

home_app = Blueprint("home_app", __name__)


@home_app.route("/", methods=["GET"])
def home():
    formats = Formats()
    return json_response(formats.convert_csv_to_json(formats.path_database("risco_credito.csv")))


# register blueprints
app.register_blueprint(home_app)
# app.register_blueprint(pet_app)

manager = Manager(app)

# Turn on debug
manager.add_command(
    "runserver",
    Server(
        use_debugger=True,
        use_reloader=True,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 3000)),
    ),
)


def json_response(obj, status_code=200, cls=None):
    response = make_response(json.dumps(obj, cls=cls), status_code)
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    manager.run()
