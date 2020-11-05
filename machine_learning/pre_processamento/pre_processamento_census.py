# -*- coding: utf-8 -*-
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

import pandas as pd
import os


def path_database(filename):
    return os.path.join(os.getcwd(), 'databases/' + filename)


base = pd.read_csv(path_database('census.csv'))
previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values

# convertendo string em numeros (categórico em integer)
previsores_labelencoder = LabelEncoder()
# label = previsores_labelencoder.fit_transform(previsores[:, 1])
previsores[:, 1] = previsores_labelencoder.fit_transform(previsores[:, 1])
previsores[:, 3] = previsores_labelencoder.fit_transform(previsores[:, 3])
previsores[:, 5] = previsores_labelencoder.fit_transform(previsores[:, 5])
previsores[:, 6] = previsores_labelencoder.fit_transform(previsores[:, 6])
previsores[:, 7] = previsores_labelencoder.fit_transform(previsores[:, 7])
previsores[:, 8] = previsores_labelencoder.fit_transform(previsores[:, 8])
previsores[:, 9] = previsores_labelencoder.fit_transform(previsores[:, 9])
previsores[:, 13] = previsores_labelencoder.fit_transform(previsores[:, 13])


# Dummy - após fazer a conversão de string para integer deve ser classificar se é ou não mensurável
# e para fazer isso deve fazer dummy para que os número não seja ordenação, sendo um maior que outro
onehotencoder = OneHotEncoder(categories='auto', sparse=False)
previsores = onehotencoder.fit_transform(previsores)

classe_labelencoder = LabelEncoder()
classe = classe_labelencoder.fit_transform(classe)

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
print(previsores)
