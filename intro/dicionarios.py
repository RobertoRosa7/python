# -*- coding: utf-8 -*-
"""
    Trabalhando com dicionários
"""
import json
import random
import itertools
from collections import defaultdict, OrderedDict, Counter
from operator import itemgetter
from databases import database, mix, strings, names, numbers, people, sequence, products


def convert_json():
    """
        Convertendo estrutura de dados json em dict pyhton
    """
    data = {"name": "Roberto", "lastname": "Rosa da Silva", "idade": 32}
    json_str = json.dumps(data)
    print(json_str)
    print(type(json_str))
    data = json.loads(json_str)
    print(data)
    print(type(data))


convert_json()


def extractingValuesFromDict():
    moreThanHundred = {key: value for key,
                       value in products.items() if value > 100}
    lessThanFifty = {key: value for key,
                     value in products.items() if value < 50}
    print("maior que R$ 100,00", moreThanHundred)
    print("menor que R$ 50,00", lessThanFifty)


def counterWords():
    """
      Usando a classe Counter para contar a quantidade de ocorrências
  """
    count = Counter(names)  # contar todas os nomes
    print(count.most_common(3))  # os dois nomes com maior ocorrência


def calc_width_dict():
    """
      Calculos com dicionários
  """
    products = {
        "Tablet": 2000,
        "Notebook": 5000,
        "Desktop": 1599,
        "Mouse": 98.98,
        "Cabo USB": 18.50,
        "Monitor": 599,
    }
    # filtro pelo menor preço
    # minPrice = min(zip(products.values(), products.keys()))
    # maxPrice = max(zip(products.values(), products.keys()))
    # print('Maior preço', maxPrice)
    # print('Menor preço', minPrice)

    # print(products.keys()) # listar todas as chaves ou propriedades
    # print(products.values()) # listar todos os valores
    print(products.keys() & people.keys())  # todas as chaves em comuns
    print(products.keys() - people.keys())  # todas as chaves que estão em


def implementsTuplas():
    """
        Implementando tuplas com a função zip - combinação de elementos de tuplas
    """
    # junção do primeiro indice o array1 com o primeiro indice do array2
    # result = zip([1,2,3], [4,5,6])
    # print(list(result))


def concat_list():
    # ajuntar duas ou mais lista
    comb = itertools.chain(strings, numbers, mix)
    print(comb)


def use_get():
    """
        Trabalhando com método get em listas
    """
    # imprime o valor da propriedade nome
    # print(people['nome'])
    if people.get("nome"):
        print("propriedade existente\n")
    else:
        print("propriedade inexistente\n")


def filterList():
    """
        Criando uma lista somente com indice pares:
    """

    # filtro de pares
    par = [x for x in range(11) if x % 2 == 0]

    # exponenciação
    exp = [x ** 2 for x in range(1, 11)]
    print(exp, par)


def intro():
    # caputrando o indice de strings
    # print(mix[3])

    # verificando o tamanho da linha
    # size = len(mix)

    # adicionado novo item na lista
    # strings.append(3)

    # remover item da lista
    # del strings[2:] # imprime somente os dois primeiros, todo resto é removido
    # del numbers[:] # remove todos os item da lista

    # verificar se existe valores na lista
    # if 'Brasil' in mix:
    #     print('esta na lista:')
    # else:
    #     print('não esta na lista:')
    """
        ordenando lista com sort()
    """
    # sorted(var) - retorna uma nova lista ordenana
    # sort() - altera a lista que já existe
    # sort(reverse=True) - retornar em ordem decrescente
    # reverse() - inverter a lista

    # stringsOrder = sorted(strings)
    # strings.sort()
    # strings.reverse()

    # print(strings)

    """
        Trabalhando com Objetos JSON
    """

    dictSites = {
        "Diego": "diegomariano.com",
        "Google": "google.com",
        "Udemy": "udemy.com",
    }
    print(dictSites["Udemy"])

    """
        Trabalhando com números aleatórios: necessário import random
        randint(indice, qtd) - números aleatórios
        seed(numero) - forçar escolha de um numero
        choice(numero) - escolhe um número aleatório dentro da lista
    """
    # numAle = random.randint(0,10) # entre 0 até 10 inteiro
    numAle = random.choice(numbers)
    print(numAle)

    """
        Trabalhando com tratamento de excessões (erros)
    """
    a = 2
    b = 0

    try:
        print(a / b)
    except:
        print("Não é possível dividir", a, "por", b)


def list():
    # percorrer uma lista de modo inverso
    # for i in reversed(sequence):
    #     print(i)

    # somente valores positivos de uma lista com valores mistos
    # print([i for i in sequence if i > 0])

    # somente os valroes negativos
    # print([i for i in sequence if i < 0]) # list comprehentions

    # list generator
    # numNative = (i for i in sequence if i < 0)
    # for a in numNative:
    #     print(a)

    # numPositive = (i for i in sequence if i > 0)
    # for a in numPositive:
    #     print(a)

    # caputrar o último elemento da lista
    # print(mix[-1])

    # total de itens da lista
    # print(len(mix))

    # concatenar lista, juntar uma na outra
    # mix.extend(strings)

    # inserir elemento em qualquer posição da lista
    # mix.insert(3, 'Beto')

    # remover qualquer elemento dentro da lista
    # mix.remove('Brasil') # através do elemento
    # mix.pop(2) # através do índice

    # limpar lista com clear
    # mix.clear()

    # identificar o índice de um elemento
    # print(mix.index('Estados Unidos'))

    # contar quantas ocorrência existe
    # print(mix.count('Brasil'))

    # ordenação de lista do dicionarios
    orderByName = sorted(database, key=itemgetter("name"))
    orderByAge = sorted(database, key=itemgetter("age"))
    print(orderByName)
    print(orderByAge)


def tuplas():
    """
        Estrutura de dados que NÃO permite alteração após sua declaração
    """
    tupla = (1, 2, 3, 4, 5)

    # adicionando contador a tupla
    for count, elem in enumerate(tupla):
        print("%d %d" % (count, elem))


def dict():
    # saber os valores através das chaves
    # print(people['nome'])

    # capturar as chaves
    # print(people.keys())

    # remover um elemento do objeto
    # del people['nome']

    # procurar por valores no objeto
    # print('Roberto' in people)

    # capturar os valores do dict
    print(people.values())


def dictMultiValue():
    """
    Dicionário de multiplus valores - uma lista de objetos, lembrando que lista são um conjunto
    de chaves com valores únicos
  """
    # não elimina repetição e precisa usar append()
    d = defaultdict(list)

    d["marcos"].append(10)
    d["marcos"].append(20)
    d["marcos"].append(30)
    d["marcos"].append(40)

    d["roberto"].append("idade")
    d["roberto"].append(30)
    d["roberto"].append(40)

    # elimina repetição e precisa usar add
    l = defaultdict(set)
    l["marcos"].add(10)
    l["marcos"].add(10)
    l["marcos"].add(10)
    l["marcos"].add(20)

    print(l["marcos"])


def orderedDict():
    """
    Ordenação de dicionários multiplus valores
  """
    order = OrderedDict()

    order["Python"] = 10
    order["CSS"] = 3
    order["HTML"] = 5
    order["JavaScript"] = 8
    order["Angular"] = 9
    order["MongoDB"] = 2
    order["Vscode"] = 7

    # loop for list ordering
    for i in order:
        print(i, order[i])
