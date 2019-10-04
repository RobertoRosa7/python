# -*- coding: utf-8 -*-
from math import sqrt

"""
    Instruções para as atividades:

    int(string) - converter string para numeros inteiro
    float(string || integer) - converter para float
    str(integer || float || tuple) - converte um inteiro para string

    ord(string) - converter caracter para inteiro
    hex(string) - converter um inteiro para string hexadecimal
    oct(string) - conveter inteiro para string octal
    tuple(string) - converter string e coloca cada caracter entre aspas simples e dentro de parênteses
    set(tuple) - converter string e coloca cada caracter entre aspas simples e dentro de chaves
    list(tuple) - converte string e coloca cada caracter entre aspas simples e dentro de colchetes

    dict(tuple) - converte tuple para um objeto, coloca cada caracter como propriedade e indice como valor
    complex(real, imag) - converte números reais para complexos

    modelo de tuplo: tup = (('a', 1), ('b', 2), ('c', 3))
"""
def enum():
    '''
        Model simples de enumeração: realiza uma associação com os índices de um array com
        os seus respectivos valores.
    '''
    list = ['a', 2, 'b', 3, 'c', 4, 'd']
    for i, value in enumerate(list):
        print(i, value)

def npv():
    '''
        valor investido R$ 100,00 hoje, e R$30,00 no próximo ano, a inflação de 3.5% será de
        R$10,00, R$40,00, R$50,00, R$45,00 e R$20,00 no final de cada ano nos próximos cinco anos,
        com início no segundo ano
    '''
    rate = 0.035
    cashflows = [-100, -30, 10, 40, 50, 45, 20]

    total = 0.0
    # sem enumerate
    # for i in range(0, len(cashflows)):
    #     total += cashflows[i] / (1 + rate) ** i

    # com enumerate
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1 + rate) ** (i + 1)
    print(total)

npv()
def fv_f():
    '''
        Calcular o valor futuro:
        deposito de R$ 100,00 hoje, com taxa de 1.5% ao ano, período de três anos
        qual será seu valor?
    '''
    pv = 100
    r = 0.015
    n = 3
    return pv*(1+r)**n

def fibonacci(n):
    '''
        É a somo do número anteriror com o próximo
        1, 1, 2, 3, 5, 8, 13, 21...
    '''
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def pot(base, expoente):
    '''
        Potenciação:
        2 ** 3 = 2 * 2 * 2 * = 8
        2 ** 0 = 1
    '''
    if expoente == 0:
        return 1
    return base * pot(base, expoente - 1)

def isPar(n):
    '''
        Verificar se o número é par
    '''
    if n % 2 == 0:
        return True
    return False

def isPrimo(n):
    '''
        Verificar se o número é primo, são inteiros que são divididos por 1 ou
        por ele mesmo
    '''
    if n == 1:
        return False

    # auxiliar para elaboração
    aux = 0
    # procurar por possiveis divisores
    for i in range(1, n + 1):
        if n % i == 0:
            aux = aux + 1

    # verificar se há ou não mais divisores
    # if aux > 2:
    #     return False
    # return True
    return False if aux > 2 else True

def maiorOuMenorIdade():
    """
        Atividade: 01
        Fazer um programa que receba a idade do usuário e verificar se é maior ou
        menor de idade.
    """
    idade = input('Digite sua idade: ')
    idade = int(idade)

    if idade > 0 and idade < 18:
        print('Você não é maior de idade')
    elif idade > 18:
        print('Você é maior de idade: ')

def nota():
    """"
        Atividade 02
        Fazer um programa que receba duas notas do  usuário, se a nota for maior ou
        igual a seis - retorne aprovado ou reprovado.
    """
    nota1 = input('Digite sua nota: ')
    nota2 = input('Digite sua segunda nota: ')
    nota1 = int(nota1)
    nota2 = int(nota2)

    if nota1 <= 10 and nota2 <= 10:
        total = somaNota(nota1, nota2)
        media = total / 2

        if media > 6:
            print('Você foi aprovado!')
        else:
            print('Você não foi aprovado!')
    else:
        print('As notas devem ser menor que dez: ')

def somaNota(nota1, nota2):
    return nota1 + nota2

def equacao(a, b, c):
    """
        Atividade 03
        Fazer um programa que resolva uma equação de segundo grau
    """
    # Model de operação de segundo grau:
    # a2 + bx +c (-b +- sqrt(b2 - 4ac)) / 2

    delta = b ** 2 - 4 * a * c
    raizDelta = sqrt(delta)
    x1 = (-b + raizDelta) / (2 * a)
    x2 = (-b - raizDelta) / (2 * a)

    print("x1 = ", x1)
    print("x2 = ", x2)

def orderList():
    """
        Atividade 04
        Fazer um programa que ordeno itens numérica na lita
    """
    # modo básico
    # list = [8, 5, 2]
    # order = sorted(list)
    # return order

    # modo manual
    lista = [8,5,2,342,2,2324,24,234,234,45,234,12,55,66,11,342,513414,0]
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        if lista[i] != lista[menor]:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux
    print(lista)

def matByUser():
    """
        Atividade 05
        Fazer um programa dois números e um sinal e faça a operação matemática pelo
        sinal recebido.
    """
    num1 = input('Digite um número\n')
    num2 = input('Digite outro número\n')
    try:
        num2 = int(num2)
        num1 = int(num1)
        operation = input('Digite qual a operação: + - x / % \n')

        result = resolveOperation(num1, operation, num2)
        print(result)
    except:
        print('Não é foi possível realizar sua operação!')

def resolveOperation(num1, operation, num2):
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '/':
            return num1 / num2
        elif operation == 'x' or operation == '*':
            return num1 * num2
        elif operation == '%':
            return num1 % num2
        elif operation == '**':
            return num1 ** num2
        else:
            return 'Não é um operador válido:'
    except:
        print('Não foi possível efeturar seu cálculo')
