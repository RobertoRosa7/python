# -*- coding: utf-8 -*-
import os, sys
from flask import Flask
# from flask_mongoengine import MongoEngine
from flask_script import Manager, Server
from flask import Blueprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
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

home_app = Blueprint("home_app", __name__)


@home_app.route("/")
def home():
    return "Hello World my first API"


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

if __name__ == "__main__":
    manager.run()
