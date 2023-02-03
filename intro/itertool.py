# -*- coding: utf-8 -*-
import itertools
from itertools import permutations
from itertools import combinations
from itertools import groupby
from operator import itemgetter
from databases import database

def createGroupByDate():
    '''
        Criando groupos e ordenando pela data
    '''
    # ordem by age
    database.sort(key=itemgetter('age'))

    # create groups
    for age, items in groupby(database, key=itemgetter('age')):
        print('idade', age)
        for i in items:
            print(' ', i)
createGroupByDate()
def groupObject():
    '''
        Agrupamento de elementos
    '''
    ex = [
        ('Marcos', 28), 
        ('Marcos', 20), 
        ('Marcos', 30), 
        ('Pedro', 19), 
        ('Joao', 20),
        ('Sandra', 35),
        ('Manoel', 18),
        ('Gustavo', 30),
        ('Leonardo', 38),
        ('Maria Luiza', 22)
    ]
    ex.sort(key=itemgetter(0)) # ordenar lista por nome
    # print(type(ex)) # imprime tipo de elemento

    # criando um json com itens agrupados
    json = {key: sorted(map(itemgetter(1), value)) for key, value in groupby(ex, key=itemgetter(0))}
    print(json)

def intertool():
    '''
        Permutations retorna todas as combinações possíveis de uma lista
    '''
    list = [1,2,3]
    # (1, 2, 3)
    # (1, 3, 2)
    # (2, 1, 3)
    # (2, 3, 1)
    # (3, 1, 2)
    # (3, 2, 1)

    # for l in permutations(list):
        # print(l)

    # for c in combinations(list, 2):
    #     print(c)

    # vinculando indices das lista com produtos cartesianos
    # for p in itertools.product([1,2,3,4], [5,6]):
    #     print(p)

    print(list)
