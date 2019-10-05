# -*- coding: utf-8 -*-
from collections import Counter

def multSet():
  '''
    Multiplicidade de objetos - {a,a,b} a tem multiplicidade de 2 e b tem multiplicidade de 1
  '''
  # não há ordenação
  c = Counter(a=2, b=3, c=5)
  c.elements()

  # lista completa
  # print(list(c.elements()))

  # todos os elementos mais comuns
  # print(c.most_common())

  # apenas os dois elementos mais comuns
  print(c.most_common(2))

multSet()