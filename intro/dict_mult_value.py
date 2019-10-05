# -*- coding: utf-8 -*-
from collections import defaultdict

def dictMultiValue():
  '''
    Dicionário de multiplus valores - uma lista de objetos, lembrando que lista são um conjunto
    de chaves com valores únicos
  '''
  # não elimina repetição e precisa usar append()
  d = defaultdict(list)

  d['marcos'].append(10)
  d['marcos'].append(20)
  d['marcos'].append(30)
  d['marcos'].append(40)

  d['roberto'].append('idade')
  d['roberto'].append(30)
  d['roberto'].append(40)

  # elimina repetição e precisa usar add
  l = defaultdict(set)
  l['marcos'].add(10)
  l['marcos'].add(10)
  l['marcos'].add(10)
  l['marcos'].add(20)

  print(l['marcos'])

dictMultiValue()