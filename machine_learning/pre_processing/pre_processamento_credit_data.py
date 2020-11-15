# -*- coding: utf-8 -*-

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os


def debug(**Kwargs):
    for key, value in Kwargs.items():
        print("key %s, value %s" % (key, value))


def path_databases(filename):
    return os.path.join(os.getcwd(), "databases/" + filename)


"""
Leitura do arquivo CSV
"""
# base = pd.read_csv(path_databases('credit_data.csv'))
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
Tratamento de valores faltantes - campos vazio ou null
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
# scaler = StandardScaler()
# previsores = base.iloc[:, 1:4].values
# previsores = scaler.fit_transform(previsores)


"""
Divisão das bases de dados de treinamento e teste
"""
base = pd.read_csv(path_databases("credit_data.csv"))
base.loc[base.age < 0, "age"] = 40.92

previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

(
    previsores_trainamento,
    previsores_teste,
    classe_treinamento,
    classe_teste,
) = train_test_split(previsores, classe, test_size=0.25, random_state=0)


debug(
    previsores_trei=previsores_trainamento,
    previsores_test=previsores_teste,
    classe_trei=classe_treinamento,
    classe_test=classe_teste,
)
