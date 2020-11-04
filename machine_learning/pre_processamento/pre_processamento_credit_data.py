# -*- coding: utf-8 -*-

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import os


def debug(**Kwargs):
    for key, value in Kwargs.items():
        print('key %s, value %s' % (key, value))


"""
Leitura do arquivo CSV
"""
base = pd.read_csv(os.path.join(
    os.getcwd(), 'databases/credit_data.csv'))
# print(base.describe())

"""
Tratamento de valores inconsistentes
"""
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
# base.loc[base.age < 0, 'age'] = 40.92
# print(base.loc[base['age'] < 0])


# Verificando se há valores null
# print(pd.isnull(base.age)) # geral
# print(base.loc[pd.isnull(base.age)])  # somente idade

"""
Tratamento de valores faltantes
"""
# fazendo a divisão entre previsores e classe dos atributos
# previsores = base.iloc[:, 1:4].values  # todas as linhas do um até o 4
# classe = base.iloc[:, 4].values

# imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# imputer = imputer.fit(previsores[:, 0:3])
# previsores[:, 0:3] = imputer.transform(previsores[:, 0:3])
# print(previsores)


"""
Escalonamento de atributos
Padronização (standardisation) x = x-média(x)/desvio_padrão(x)
Normalização (normalization) x = x-mínimo(x)/máximo(x)-mínimo(x)
"""
scaler = StandardScaler()
previsores = base.iloc[:, 1:4].values
previsores = scaler.fit_transform(previsores)
