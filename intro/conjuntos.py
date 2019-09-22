# -*- coding: utf-8 -*-

def conjunto():
    '''
        Conjunto de dados que não permite repetição de dados
    '''
    # conjunto
    conj = {2,2,4,4,'Beto','Beto','Marco','Marco'}

    # conveter lista para conjunto
    list = [2,3,4,1,4,4,2,3,'Beto','Beto','Sandra',3,2,4,'Sandra']
    listToConj = set(list)

    # adicionar elemento no conjunto
    # conj.add('Osasco')

    # remover elemento no conjunto
    conj.remove('Beto')
    print(conj)

conjunto()
