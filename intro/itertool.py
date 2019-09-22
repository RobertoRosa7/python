# -*- coding: utf-8 -*-
from itertools import permutations
from itertools import combinations

def itertool():
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

    for c in combinations(list, 2):
        print(c)

# itertool()
