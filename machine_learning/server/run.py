# -*- coding: utf-8 -*-
import json
import os, sys
import numpy as np

sys.path.append(os.path.abspath(os.getcwd()))

from flask import Flask

# from flask_mongoengine import MongoEngine
from flask_script import Manager, Server
from machine_learning.server.app.pages.home.home import home2
from machine_learning.server.routes.routes import home_app, naive_bayes_risco_credito

# db = MongoEngine()

app = Flask(__name__)
# app.config.from_pyfile("settings.py")

# apply overrides for test
app.config.update()

# set db
# db.init_app(app)

# register blueprints
app.register_blueprint(home_app)
app.register_blueprint(naive_bayes_risco_credito)
app.register_blueprint(home2)

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
