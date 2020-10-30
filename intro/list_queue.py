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

    def pop(self):
        # remove item
        return heapq.heappop(self._queue)[-1]


class Person():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


priority = ListQueue()
priority.push(Person('Kakashi'), 4)
priority.push(Person('Maria'), 3)
priority.push(Person('Camila'), 5)
priority.push(Person('Gabriela'), 2)

# return camila porque tem maior prioridade
print(priority.pop())
