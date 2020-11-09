import os, sys
sys.path.append(os.path.abspath(os.getcwd()))

from flask import Blueprint
from utils.formats import Formats
from machine_learning.naive_bayes.naive_bayes_risco_credito import classificador


home_app = Blueprint("home_app", __name__)
naive_bayes_risco_credito = Blueprint("naive_bayes_risco_credito", __name__)

@home_app.route("/", methods=["GET"])
def home():
    formats = Formats()
    return formats.json_response(
        formats.convert_csv_to_json(formats.path_database("risco_credito.csv"))
    )


@naive_bayes_risco_credito.route("/naive_bayes_risco_credito", methods=["GET"])
def fn_naive_bayes_risco_credito():
    formats = Formats()
    return formats.json_response({"classification": list(classificador())})