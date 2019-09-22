# -*- coding: utf-8 -*-
import markdown
import os

# import from framework flask
from flask import Flask
from pymongo import MongoClient
from random import randint

# create an instance of flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     # return 'Welcome to Python Flask API'
#
#     #open the README file
#     with open(os.path.dirname(app.root_path) + '/api/README.md', 'r') as markdown_file:
#         # read the content
#         content = markdown_file.read()
#
#         # convert to html
#         return markdown.markdown(content)

def teste_connect():
    try:
        #MONGO_URI = 'mongodb+srv://kakashi:pzpzhsr&2602@blog-ssr02.mongodb.net/test?retryWrites=true&w=majority'
        #MONGO_URI = 'mongodb://127.0.0.1:27017'
        client = MongoClient(port=27017)

        # print(client)
        db = client.business
        names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
        company_type = ['LLC','Inc','Company','Corporation']
        company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
        for x in range(1, 501):
            business = {
                'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
                'rating' : randint(1, 5),
                'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
            }
            #Step 3: Insert business object directly into MongoDB via isnert_one
            result=db.reviews.insert_one(business)
            print('Created {0} of 500 as {1}'.format(x,result.inserted_id))

        print('finished creating 500 business reviews')
    except Exception as e:
        print(e)

def get_data():
    try:
        client = MongoClient(port=27017)
        db = client.business
        fivestar = db.reviews.find_one({'rating': 5})
        print(fivestar)
    except Exception as e:
        print(e)
get_data()
