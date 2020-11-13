# -*- coding: utf-8 -*-
from datetime import datetime
import os, sys, re
import numpy as np
import pandas as pd
import json
import csv
import random

sys.path.append(os.path.abspath(os.getcwd()))
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from utils.formats import Formats
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.impute import SimpleImputer
from keras.models import Sequential
from keras.layers import Dense
from tensorflow import keras

payload = {}
accumulated = list()
formats = Formats()


def converte_json_to_csv():
    # dcsv = pd.read_csv(os.path.join(os.getcwd(), 'databases/mega.csv'))
    # djson = pd.read_json(os.path.join(os.getcwd(), 'databases/mega.json'))
    # dataCsv = dataJson.to_csv(os.path.join(os.getcwd(), 'databases/mega.csv'), index=None)

    with open(formats.path_database("mega.json"), "r") as f:
        to_python = json.loads(f.read())
        with open(formats.path_database("mega.csv"), "w") as fcsv:
            fs = csv.writer(fcsv)
            fs.writerow(["id", "ticket", "date", "concurso", "created_at"])
            for i, data in enumerate(to_python["mega"]):
                fs.writerow(
                    [
                        i,
                        data["content"],
                        data["date"],
                        data["concurso"],
                        data["create_at"],
                    ]
                )
        fcsv.close()
    f.close()


def removeLines(id_line):
    lines = list()
    with open(formats.path_database("mega.csv"), "r") as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == str(id_line):
                    lines.remove(row)
    readFile.close()

    with open(formats.path_database("mega.csv"), "w") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    writeFile.close()


def create_csv_mega(payload):
    with open(formats.path_database("mega.csv"), "rb") as readFile:
        lines = len(readFile.readlines())
        with open(formats.path_database("mega.csv"), "a") as writeFile:
            writer = csv.writer(writeFile)
            if lines > 0:
                writer.writerows(payload)
            else:
                writer.writerow(
                    ["data", "bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6"]
                )
                writer.writerows(payload)
        writeFile.close()
    readFile.close()
    print("Done!")


def megaSenaResults():
    df = pd.read_excel(formats.path_database("mega_sena_resultados.xlsx"))
    df.columns = map(str.lower, df.columns)  # tolowercase columns

    """
      conversão de datatime
    """
    # df["data_datetime"] = pd.to_datetime(df.iloc[:, 1])
    # df["day"] = df.data_datetime.dt.day
    # df["month"] = df.data_datetime.dt.month
    # df["year"] = df.data_datetime.dt.year

    # print(df.shape) # (2322 lines, 8 columns)
    # print(df.dtypes) # show type of variables

    """
      fazendo higienização dataframe
    """
    # msno.matrix(
    #     df=df.iloc[:, 0 : df.shape[1]], figsize=(20, 5), color=(0.42, 0.1, 0.05)
    # )

    """
      verificando se alguma resultado repetido
    """
    # df.groupby(["bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6"]).size().sort_values(ascending=False)

    """
      as seis dezendas mais sorteadas
    """
    dezenas = pd.DataFrame(
        df["bola 1"].tolist()
        + df["bola 2"].tolist()
        + df["bola 3"].tolist()
        + df["bola 4"].tolist()
        + df["bola 5"].tolist()
        + df["bola 6"].tolist(),
        columns=["numbers"],
    )
    col = dezenas["numbers"].value_counts().sort_values(ascending=True).head(6)

    previsores = df.iloc[:, 0:6].values
    classe = df.iloc[:, 6].values

    encoder_previsores = LabelEncoder()
    previsores[:, 1] = encoder_previsores.fit_transform(previsores[:, 1])

    (
        previsores_treinamento,
        previsores_teste,
        classe_treinamento,
        classe_teste,
    ) = train_test_split(previsores, classe, test_size=0.33, random_state=8)

    # criando model
    model = Sequential()
    model.add(Dense(10, input_dim=6, activation="relu"))
    model.add(Dense(12, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))

    # compilando model
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    # treinando model
    model.fit(
        keras.backend.cast_to_floatx(previsores_treinamento),
        keras.backend.cast_to_floatx(classe_treinamento),
    )
    # validando model
    # scores = model.evaluate(classe_teste, previsores_teste)
    scores = model.evaluate(
        keras.backend.cast_to_floatx(previsores_treinamento),
        keras.backend.cast_to_floatx(classe_treinamento),
    )
    print((model.metrics_names[1], scores[1] * 100))

    # 1 tem change 0 não tem
    # numero_sorteio = [[7, 14, 47, 54, 56, 60]]
    # predict_class = model.predict_classes(pd.DataFrame(numero_sorteio))

    # predict_proba = model.predict(pd.DataFrame(numero_sorteio))
    # print("Probablidade: ", round((predict_proba[0][0] * 100), 2), "%")
    execute_proba(df, model)


def execute_proba(df, model):
    random.seed(60)
    probe_good = 99
    probe_current = 0

    tickets = df[
        ["bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6"]
    ].values.tolist()

    while probe_current < probe_good:
        dezenas_mega = random.sample(range(1, 60), 6)
        if not dezenas_mega in tickets:
            probe_current = int(model.predict(pd.DataFrame([dezenas_mega]))[0][0] * 100)
            # print(probe_current) # Probabilidade de 99 % -> Dezenas: [3, 8, 15, 46, 47, 57]
        # Probabilidade de 99 % -> Dezenas: [10, 15, 17, 19, 20, 37]
        print(
            "Probabilidade de {0} % -> Dezenas: {1}".format(
                probe_current,
                sorted(dezenas_mega),
            )
        )


def initialize_analysis(df):
    previsores = df.iloc[0:1000, 1:7].values
    classe = df.iloc[0:1000, 6].values

    encoder_previsores = LabelEncoder()
    previsores[:, 0] = encoder_previsores.fit_transform(previsores[:, 0])

    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    imputer = imputer.fit(previsores[:, 1:7])
    previsores[:, 1:7] = imputer.transform(previsores[:, 1:7])

    (
        previsores_treinamento,
        previsores_teste,
        classe_treinamento,
        classe_teste,
    ) = train_test_split(previsores, classe, test_size=0.33, random_state=8)

    model = Sequential()
    model.add(Dense(10, input_dim=6, activation="relu"))
    model.add(Dense(12, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(previsores_treinamento, classe_treinamento)
    scores = model.evaluate(previsores_treinamento, classe_treinamento)

    # model.fit(previsores_teste, classe_teste)
    # scores = model.evaluate(previsores_teste, classe_teste)

    print((model.metrics_names[1], scores[1] * 100))
    execute_proba(df, model)


def initialize():
    df = pd.read_csv(formats.path_database("mega.csv"))
    last_date = df[-1:]["data"].values[0]  # 2020-11-12
    current_date = str(datetime.today().isoformat())[0:10]

    if last_date == current_date:
        initialize_analysis(df)
    else:
        print("update databases...")


# area de chamadas das funções
# create_csv_mega(formats.create_payload_model_mega(1000000))
initialize()