# -*- coding: utf-8 -*-
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import numpy as np
import os


def path_databases(filename):
    return os.path.join(os.getcwd(), "databases/" + filename)


# importando arquivo pra leitura
base = pd.read_csv(path_databases("credit_data.csv"))

# tratando valores menores que zero e aplicando idade média
base.loc[base.age < 0, "age"] = 40.92  # base.age[base.age > 0].mean())

# separando previsores e classe
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4]

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(previsores[:, 1:4])

# tratando de campos null
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

scaler = StandardScaler()
# tratando padronização
previsores = scaler.fit_transform(previsores)

(
    previsores_trainamento,
    previsores_teste,
    classe_treinamento,
    classe_teste,
) = train_test_split(previsores, classe, test_size=0.25, random_state=0)

classificador = GaussianNB()
classificador = classificador.fit(previsores_trainamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

# print(precisao) # percentual de acerto comparando classe_teste mais previsoes
print(pd.DataFrame(matriz))