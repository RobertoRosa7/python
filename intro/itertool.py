# -*- coding: utf-8 -*-
import itertools
from itertools import permutations
from itertools import combinations

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
