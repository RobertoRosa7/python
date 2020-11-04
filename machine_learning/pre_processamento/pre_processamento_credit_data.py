# -*- coding: utf-8 -*-

import pandas as pd
import os


def debug(**Kwargs):
    for key, value in Kwargs.items():
        print('key %s, value %s' % (key, value))


base = pd.read_csv(os.path.join(
    os.getcwd(), 'databases/credit_data.csv'))
# print(base.describe())


# base - mostra a tabela de dados - DataFrame
# base.describe() - faz uma prévia análise descrevendo com porcentagem

# Localizar atributos inconsistente idade
# print(base.loc[base['age'] < 0])

# Apagar coluna inteira
# base.drop('age', 1, inplace=True)

# Apagar somente dados inconsistentes
# base.drop(base[base.age < 0].index, inplace=True)
# print(base.loc[base['age'] < 0])

# Preencher os valores manualmente ou preencher idade com a média de idades
# print(base.mean()) # todos as colunas
# print(base.age.mean()) # somente a média de idade
# print(base.age[base.age > 0].mean()) # base média de idade sem atributos inconsistente


# Atualizar registro todas idades abaixo de zero
base.loc[base.age < 0, 'age'] = 40.92
# print(base.loc[base['age'] < 0])
