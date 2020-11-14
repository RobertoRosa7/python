# -*- coding: utf-8 -*-
import os, sys
from os.path import dirname, join
import pandas as pd

sys.path.append(os.path.abspath(os.getcwd()))

from sklearn.preprocessing import LabelEncoder
from utils.formats import Formats
from sklearn.tree import DecisionTreeClassifier, export_graphviz

formats = Formats()
df = pd.read_csv(formats.path_database("risco_credito.csv"))
previsores = df.iloc[:, 0:4].values
classe = df.iloc[:, 4].values

# Árvores de decisão não podem ser categoricos
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 1] = labelencoder.fit_transform(previsores[:, 1])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])

decisionTree = DecisionTreeClassifier(criterion="entropy")
"""
  Attributes
  -----------
    feature_importances_ : classificar a importância de cada atributo
  
  Methods
  -------
    export_graphviz : dot_data : string
      representação gráfica da árvore de decisção
"""
decisionTree = decisionTree.fit(previsores, classe)
# export_graphviz(
#     decisionTree,
#     out_file=os.path.abspath(join(dirname(os.getcwd()), 'python/tree_credit_risk.dot')),
#     feature_names=["historia", "divida", "garantias", "renda"],
#     class_names=["alto", "moderado", "baixo"],
#     filled=True,
#     leaves_parallel=True,
# )
result = decisionTree.predict([[0, 0, 1, 2], [3, 0, 0, 0]])
print(result)