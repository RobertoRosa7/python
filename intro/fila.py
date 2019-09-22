# -*- coding: utf-8 -*-
from collections import deque

def fila():
    '''
        Trabalhando com filas - deque
        se for inserido mais do que o limite o primeiro elemento será removido
        append() - adiciona no final
        appendleft() - adiciona no inicio
        pop() - remover elemento no final da fila
        popleft() - remover no inicio da fila
    '''
    fila = deque(maxlen=4)
    fila.append(1)
    fila.append(2)
    fila.append(3)
    fila.append(4)
    fila.append(5)

    # fila.popleft()
    # fila.pop()
    print(fila)

fila()
