# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import jsonify, request, abort

class PetAPI(MethodView):
    pets = [
        {'id': 1, 'name': u'Mac'},
        {'id': 2, 'name': u'Brownie'},
        {'id': 3, 'name': u'Charlie'},
        {'id': 4, 'name': u'Sansao'}
    ]

    def get(self):
        return jsonify({'pets': self.pets})