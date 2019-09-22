# -*- coding: utf-8 -*-
import heapq

def fnHeapq():
  '''
    Descobrindo quais valores tem maior ou menor valor:
    a lib heapq filtra os menores ou maiores valres
  '''
  idades = [10,14,12,23,84,23,55,23,58,49,6]

  # os três menores números
  # print(heapq.nsmallest(3, idades))

  # os três maiores números
  # print(heapq.nlargest(3, idades))

  # transformar uma lista em heap - return 6
  # heapq.heapify(idades)
  # print(idades[0])

  # remover o menor valor da lista heap
  # print(heapq.heappop(idades))

  # add value on list heap
  heapq.heappush(idades, 3)
  print(idades)


fnHeapq()