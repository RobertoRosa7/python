# -*- coding: utf-8 -*-
import heapq

class ListQueue():
  
  def __init__(self):

    '''
      Criando uma lista de prioridade em python
      push - para inserção
      pop - para remoção
    '''
    self._queue = []
    self._index = 0

  def push(self, item, priority):
    # add item
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1
  
  def pop(self, item, priority):
    # remove item
    return heapq.heappop(self._queue)[-1]