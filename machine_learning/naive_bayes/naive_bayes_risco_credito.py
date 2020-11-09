# -*- coding: utf-8 -*-
import os, sys

sys.path.append(os.path.abspath(os.getcwd()))
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from utils.formats import Formats

import pandas as pd


def classificador():
    formats = Formats()

    base = pd.read_csv(formats.path_database("risco_credito.csv"))
    previsores = base.iloc[:, 0:4].values
    classe = base.iloc[:, 4].values

    labelencoder = LabelEncoder()
    previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
    previsores[:, 1] = labelencoder.fit_transform(previsores[:, 1])
    previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
    previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])

    classificador = GaussianNB()
    classificador.fit(previsores, classe)  # gerar tabela de probalilidade
    # historia: boa, divida: alta, garantias:nenhuma, renda: > 35
    # historia: ruim, divida: alta, garantias: adequada, renda: < 15

    resultado = classificador.predict([[0, 0, 1, 2], [3, 0, 0, 0]])
    # print(pd.DataFrame(resultado))
    # print(classificador.classes_)  # mostrar as classes do classificador
    # print(classificador.class_count_)
    # print(classificador.class_prior_)  # probabilidade priori
    return resultado
