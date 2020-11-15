# -*- coding: utf-8 -*-
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import os


def path_database(filename):
    return os.path.join(os.getcwd(), 'databases/' + filename)


def debug(**Kwargs):
    for key, value in Kwargs.items():
        print('key %s, value %s' % (key, value))


base = pd.read_csv(path_database('census.csv'))
# 0:100 prevent the kernel buffer overflow
previsores = base.iloc[0:1000, 0:14].values
classe = base.iloc[0:1000, 14].values

# convertendo string em numeros (categórico em integer)
labelencoder_previsores = LabelEncoder()
# label = labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder_previsores.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder_previsores.fit_transform(previsores[:, 6])
previsores[:, 7] = labelencoder_previsores.fit_transform(previsores[:, 7])
previsores[:, 8] = labelencoder_previsores.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[:, 9])
previsores[:, 13] = labelencoder_previsores.fit_transform(previsores[:, 13])


# Dummy - após fazer a conversão de string para integer deve ser classificar se é ou não mensurável
# e para fazer isso deve fazer dummy para que os número não seja ordenação, sendo um maior que outro
onehotencoder = OneHotEncoder(categories='auto', sparse=False)
previsores = onehotencoder.fit_transform(previsores)

labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

previsores_trei, previsores_test, classe_trei, classe_test = train_test_split(
    previsores, classe, test_size=0.15, random_state=0)


debug(previsores_trei=previsores_trei, previsores_test=previsores_test,
      classe_trei=classe_trei, classe_test=classe_test)
