# -*- coding: utf-8 -*-
import os, sys
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath(os.getcwd()))

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from utils.formats import Formats

ft = Formats()

df = pd.read_csv(ft.path_database("credit_data.csv"))
df.loc[df.age < 0, "age"] = 40.92  # df.age[df.age > 0].mean())

previsores = df.iloc[:, 1:4].values
classe = df.iloc[:, 4]

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

# classificador = GaussianNB()
# classificador = classificador.fit(previsores_trainamento, classe_treinamento)
# previsoes = classificador.predict(previsores_teste)
# precisao = accuracy_score(classe_teste, previsoes)
# matriz = confusion_matrix(classe_teste, previsoes)

# print(pd.DataFrame(matriz))


decisionTree = DecisionTreeClassifier(criterion="entropy", random_state=0)
decisionTree = decisionTree.fit(previsores_trainamento, classe_treinamento)
forecast = decisionTree.predict(previsores_teste)
precision = accuracy_score(classe_teste, forecast)
matrix = confusion_matrix(classe_teste, forecast)

print(precision)