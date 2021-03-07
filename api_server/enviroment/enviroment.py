import os, sys

sys.path.append(os.path.abspath(os.getcwd()))

from pymongo import MongoClient


def set_mode(dev_mode=True):
  return dev_mode

mode = set_mode()

# PRIMEIROAPP_API = os.environ.get('PRIMEIROAPP_API_DEV') if mode else os.environ.get('PRIMEIROAPP_API_PROD')

PRIMEIROAPP_API_DEV = os.environ.get('PRIMEIROAPP_API_DEV')
PRIMEIROAPP_API_PROD = os.environ.get('PRIMEIROAPP_API_PROD')

conn = MongoClient(host=PRIMEIROAPP_API_PROD, port=27017)

# client = MongoClient("mongodb+srv://beto:beto1234@cluster0.rt58f.mongodb.net/primeiroapp?retryWrites=true&w=majority")
# client = MongoClient("mongodb://beto:beto123@cluster0-shard-00-00.rt58f.mongodb.net:27017,cluster0-shard-00-01.rt58f.mongodb.net:27017,cluster0-shard-00-02.rt58f.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-xu6lpq-shard-0&authSource=admin&retryWrites=true&w=majority")
# db = client.test
# print(client.list_database_names())

db = conn['primeiroapp']