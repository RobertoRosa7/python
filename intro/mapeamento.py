# -*- coding: utf-8 -*-

"""
  Usando python para fazer mapeamento de dados
"""
from collections import ChainMap


def makeMaping():
  """
    Se hover chaves duplicadas o valor da chave que vier primeiro será considerada
  """
  a = {'x': 1, 'z': 3}
  b = {'y': 2, 'z': 4}

  c = ChainMap(a, b)
  print(c['z'])


makeMaping()
