# -*- coding: utf-8 -*-

def strings():
    '''
        Manipulação de strings
    '''

    # acessar cada caracter
    # nome = 'roberto'

    # substituir algum caracter por outro
    nome = 'roberto'
    lista = list(nome)
    lista[0] = 't'
    nome = ''.join(lista)

    print(nome)

strings()
