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


def create_csv_mega(payload, filename):
    if not formats.is_file_exists(filename):
        with open(formats.path_database(filename), "a") as new_file:
            writer = csv.writer(new_file)
            writer.writerow(
                ["data", "bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6"]
            )
            writer.writerows(payload)
    else:
        with open(formats.path_database(filename), "rb") as readFile:
            lines = len(readFile.readlines())
            with open(formats.path_database(filename), "a") as writeFile:
                writer = csv.writer(writeFile)
                if lines > 0:
                    writer.writerows(payload)
                else:
                    writer.writerow(
                        [
                            "data",
                            "bola 1",
                            "bola 2",
                            "bola 3",
                            "bola 4",
                            "bola 5",
                            "bola 6",
                        ]
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


def initialize(filename):
    df = pd.read_csv(formats.path_database(filename))
    df.columns = map(str.lower, df.columns)  # tolowercase columns
    last_date = df[-1:]["data"].values[0]  # 2020-11-12
    current_date = str(datetime.today().isoformat())[0:10]

    if last_date == current_date:
        initialize_analysis(df)
    else:
        print("update databases...")
        create_csv_mega(formats.create_payload_model_mega(1000, "mega.csv"), "mega.csv")


def initialize_analysis(df):
    previsores = df.iloc[:, 1:7].values
    classe = df.iloc[:, 6].values

    encoder_previsores = LabelEncoder()
    previsores[:, 0] = encoder_previsores.fit_transform(previsores[:, 0])

    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    imputer = imputer.fit(previsores[:, 1:7])
    previsores[:, 1:7] = imputer.transform(previsores[:, 1:7])
    asDezenasMaisRepetidas = []
    for c in df.columns:
        if c.startswith("bola"):
            asDezenasMaisRepetidas.append(
                df[c].value_counts().sort_values(ascending=True).index[0]
            )

    print("As seis dezenas mais repetidas {0}".format(sorted(asDezenasMaisRepetidas)))

    (
        previsores_treinamento,
        previsores_teste,
        classe_treinamento,
        classe_teste,
    ) = train_test_split(previsores, classe, test_size=0.33, random_state=8)

    print("Calculando a probabilidade...")

    model = Sequential()
    model.add(Dense(10, input_dim=6, activation="relu"))
    model.add(Dense(12, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(previsores_treinamento, classe_treinamento)
    scores = model.evaluate(previsores_treinamento, classe_treinamento)

    print((model.metrics_names[1], scores[1] * 100))
    print(
        "Probabiliade sobre as seis dezenas: {0} % {1}".format(
            round(
                float(
                    model.predict(pd.DataFrame([asDezenasMaisRepetidas]))[0][0] * 100
                ),
                2,
            ),
            sorted(asDezenasMaisRepetidas),
        )
    )
    execute_proba(df, model)


def execute_proba(df, model):
    probe_good = 99
    probe_current = 0

    tickets = df[
        ["bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6"]
    ].values.tolist()

    # df_mega = pd.read_excel(formats.path_database("mega_sena_resultados.xlsx"))
    # df_mega.columns = map(str.lower, df_mega.columns)  # tolowercase columns
    # tickets = df_mega[
    #     ["bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6"]
    # ].values.tolist()

    while probe_current < probe_good:
        dezenas_mega = formats.otherWayToGenerateArray(6)[1:]
        if not dezenas_mega in tickets:
            probe_current = float(
                model.predict(pd.DataFrame([dezenas_mega]))[0][0] * 100
            )
            # print(probe_current) # Probabilidade de 99 % -> Dezenas: [3, 8, 15, 46, 47, 57]
        else:
            probe_current = float(
                model.predict(pd.DataFrame([dezenas_mega]))[0][0] * 100
            )
            print("dezenda encontrada na base de dados: {0}".format(dezenas_mega))

        # Probabilidade de 99 % -> Dezenas: [10, 15, 17, 19, 20, 37]
        print(
            "Probabilidade de {0} % -> Dezenas: {1}".format(
                round(probe_current, 2),
                sorted(dezenas_mega),
            )
        )


def convertExcelMegaSenaToCsv(filename):
    try:
        df = pd.read_excel(formats.path_database(filename))
        df.columns = map(str.lower, df.columns)  # tolowercase columns
        df["data"] = pd.to_datetime(df["data"])

        predicts = df.iloc[:, 1:8].values.tolist()
        print(predicts)
        return predicts
    except AttributeError:
        print("File not suported")


# area de chamadas das funções
# initialize("teste.csv")
# convertExcelMegaSenaToCsv("mega_sena_resultados.xlsx")
# create_csv_mega(convertExcelMegaSenaToCsv("mega_sena_resultados.xlsx"),"teste.csv")

df = pd.read_csv(formats.path_database("teste.csv"))
dateLast = df.sort_values("data", ascending=False)[-1:]["data"].values[0]
dateFirst = df.sort_values("data", ascending=True)[-1:]["data"].values[0]

dateMediaFirst = formats.getPeriod(5, dateLast, dateFirst)["dateMediaFirst"]
dateMediaLast = formats.getPeriod(5, dateLast, dateFirst)["dateMediaLast"]

df.loc[
    (df["data"] <= dateMediaFirst) & (df["data"] >= dateMediaLast), "proba"
] = "moderate"

df.loc[(df["data"] > dateMediaFirst) & (df["data"] <= dateFirst), "proba"] = "low"
df.loc[(df["data"] >= dateLast) & (df["data"] < dateMediaLast), "proba"] = "high"

moderate = df.loc[(df["data"] <= dateMediaFirst) & (df["data"] >= dateMediaLast)]
low = df.loc[(df["data"] > dateMediaFirst) & (df["data"] <= dateFirst)]
high = df.loc[(df["data"] >= dateLast) & (df["data"] < dateMediaLast)]

print(high)
