# -*- coding: utf-8 -*-

"""
    Trabalhando com arquivos:
    Abrir:
    open(nome, modo)
    modo:
        r: somente leitur
        w: gravação, gera novo arquivo vazio, sobreescreve existentes
        a: leitura e escrita, adiciona novo conteúdo no fim do arquivo
        r+: leitura e escrita
        w+: escrita
        a+: leitura e escrita - abre o arquivo para atualização

    Ler:
    read() - lê arquivo inteiro
    readline() - lê apenas uma linha
    readelines() - lê o arquivo e gera nova lista (array)
"""
import random


def first():
    # Nova instancia para conter todo conteúdo do arquivo
    file = open('arquivo_teste.txt')

    # criar novo arquivo existentes
    file2 = open('arquivo_este2.txt', 'a')

    # gravar dados no arquivos
    # file2.write('este arquivo foi criado com python')

    # adicionando novo alinha no final do arquivo
    file2.write('este é uma nova linha com python usando (modo a)\n')

    # ler todo conteúdo do arquivo e criar uma lista - array
    lines = file.readlines()
    line = file.readline()
    text = file.read()

    # lendo linha por linha
    # for line in lines:
    #     print(line)

    # print(lines)

    # sempre que abrir um arquivo deve ser fechado
    file.close()
    file2.close()


def second():
    # abrir arquivo com alias
    with open('arquivo_este2', 'r') as f:
        print(f.read())
    f.close()  # importante fechar sempre que abrir um arquivo


def third():
    # escrendo arquivo
    with open('arquivo_teste3.txt', 'w') as f:
        f.write('Este arquivo foi escrito pelo python:\n')
    f.close()


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(7)) # return 13

def calc_sum(list_a, list_b):
    return [(v1 + v2) for v1, v2 in zip(list_a, list_b)]


def calc_sum2(list_a, list_b):
    return list(map(lambda v1, v2: v1 + v2, list_a, list_b))


def calc_sum3(list_a, list_b):
    return list(map(sum, zip(list_a, list_b)))


def generate_range(size):
    lists = []
    for i in range(size):
        lists.append(random.randint(0, 9))
    return lists


num = calc_sum3(generate_range(10), generate_range(10))
print(num)
