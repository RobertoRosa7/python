# -*- coding: utf-8 -*-

class Pessoas:
    '''
        Classe - Orientação á objetos
        self: igual ao this que representa este objeto da classe
    '''

    # método construtor de python
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

def createUser():
    pessoa1 = Pessoas('Roberto')
    pessoa2 = Pessoas('Sandra')
    pessoa3 = Pessoas('Camila')

    # imprimir o nome
    # print(pessoa3.getName())

    # alterar o nome
    pessoa1.setName('Roberto Rosa')
    print(pessoa1.getName())


class SomentePares(numbers):
    '''
        Classe - Somente pares, retornar somentes números pares
    '''

    def append(self, integer):
        if not isistance(integer, int):
            raise TypeError('Use somente números inteiros: ex: 1,2,3')
