# -*- coding: utf-8 -*-
import math
# import module # importação normal
# from module import * # importação total não precisar usar module.fn
from databases import sequence

def rootSquare():
    # root square for number more than 3 - method comprehention
    print([math.sqrt(i) for i in sequence if i >= 5])

rootSquare()
def mathsOperations():
    """
        Operações matemática
    """

    # adição
    print('adição: ', 2 + 2)

    # subtração
    print('subtração: ', 2 - 1)

    # multiplicação
    print('multiplicação: ', 2 * 2)

    # divisão
    print('divisão: ', 10 / 2)

    # módulo - resto da divisão
    print("módulo: ", 10 % 3)

    # exponenciação
    print('potenciação: ', 2 ** 3)

    # arredontamento para interio - cima
    print(math.ceil(3.2)) # return 4

    # erredontamento para inteiro - abaixo
    print(math.floor(3.2)) # return 3

    # número absoluto
    print(math.fabs(-5)) # return 5.0

    # fatorial - multiplicação de forma recursiva
    print(math.factorial(3)) # return 6

    # exponenciação 2 elevado 10
    print(math.pow(2, 10)) # return 1024

    # logaritmo
    print(math.log(10)) # return 1.922

    # raiz quadrada
    print(math.sqrt(25)) # return 5

    # cosceno
    print(math.cos(10)) # return -0.894

    # radiano
    print(math.sin(10)) # return -0.54

    # PI
    print(math.pi)

# executando funções do módulo aqui neste script
# print(module.media(10, 20))