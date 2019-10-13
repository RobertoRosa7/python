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


class SomentePares(list):
    '''
        Classe - Somente pares, retornar somentes números pares
    '''
    def append(self, inteiro):
        if not isinstance(inteiro, int):
            raise TypeError('Use somente números inteiros: ex: 1,2,3')
        if inteiro % 2:
            raise ValueError('Use somente números divididos por 2')

        super().append(inteiro)


def errorDivision(divider):
    '''
        Trabalhando com tratamento de possíveis erros
    '''
    try:
        if divider == 13:
            raise ValueError('13 não é legal!')
        return 10 / divider
    except ZeroDivisionError:
        return 'Divisão por zero não possível'
    except TypeError:
        return 'Entre com um valor numérico'
    except ValueError:
        print('Não use o número 13')
        raise

def returnChaveByArgs(**kwargs):
    '''
        Retornar um dicionário de chave/valor como argumentos - não funciona
        quando estava dentro da classe
    '''
    # print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

def anyFunc(*args):
    '''
        Função qualquer que define uma quantidade de parâmetros qualquer -
        quando chamada torna-se argumentos passados.
    '''
    print(args)
