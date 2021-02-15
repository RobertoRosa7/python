import os, sys

sys.path.append(os.path.abspath(os.getcwd()))

from pymongo import MongoClient

db = MongoClient(host="mongodb://localhost:27017", port=27017)


def get_collection(name):
    return db.primeiroapp.get_collection(name)