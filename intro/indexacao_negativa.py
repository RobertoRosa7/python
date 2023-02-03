# -*- coding: utf-8 -*-

def indexNative():
    '''
      Indexação negativa:

    '''
    lista = [1, 2, 3, 4, 2, 4, 3, 6, 7, 31, 77, 7, 3, 445, 23]

    # último elemento
    print(lista[-1], '- último elemento')

    # penultimo elemento
    print(lista[-2], '- penúltimo elemento')

    # antepenultimo elemento
    print(lista[-3], '- antepenúltimo elemento')

    # compasso de dois
    print(lista[::-2], '- compasso de dois')


indexNative()
