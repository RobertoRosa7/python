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

    # listar todos os dados
    def get(self):
        return jsonify({'pets': self.pets}), 200

    # criar um novo 
    def post(self):
        # verificação básica de dados inicial
        if not request.json or not 'name' in request.json:
            abort(400)
        pet = {
            "id": len(self.pets) + 1,
            "name": request.json["name"]
        }
        self.pets.append(pet)
        return jsonify({'pet': pet}), 201