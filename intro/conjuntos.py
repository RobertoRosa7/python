# -*- coding: utf-8 -*-

def conjunto():
    '''
        Conjunto de dados que não permite repetição de dados
    '''
    # conjunto
    conj = {2,2,4,4,'Beto','Beto','Marco','Marco'}
    conj2 = {2,4,5,2,4,2,'Beto','Sandra'}

    # conveter lista para conjunto
    list = [2,3,4,1,4,4,2,3,'Beto','Beto','Sandra',3,2,4,'Sandra']
    set(list)

    # adicionar elemento no conjunto
    # conj.add('Osasco')

    # remover elemento no conjunto
    # conj.remove('Beto')

    # imprime ambos os conjuntos - mas não repete os elementos
    # print(conj | conj2)

    # imprime somente os elemento repetidos
    # print(conj & conj2)

    # imprime somente os elementos que não estão em ambos
    # print(conj ^ conj2)

    # imprime os elementos que estão em conj, mas não estão em conj2
    print(conj - conj2)

conjunto()
