# -*- coding: utf-8 -*-
import os, sys, re
import numpy as np
from numpy.lib.function_base import delete
import pandas as pd
import json
import csv

sys.path.append(os.path.abspath(os.getcwd()))

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from utils.formats import Formats
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.impute import SimpleImputer

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


def writeTickets(payload_csv):
    with open(formats.path_database("teste.csv"), "rb") as readFile:
        lines = len(readFile.readlines())
        with open(formats.path_database("teste.csv"), "a") as writeFile:
            writer = csv.writer(writeFile)
            if lines > 0:
                for row in payload_csv:
                    writer.writerow(row)
            else:
                writer.writerow(
                    ["id", "ticket", "date", "concurso", "created_at", "repeated"]
                )
                for row in payload_csv:
                    writer.writerow(row)

        writeFile.close()
    readFile.close()
    print("Done!")


def update_csv_file():
    print("updating...")
    temp = list()
    array = list()
    new_array = list()

    with open(formats.path_database("teste.csv"), "r") as rf:
        for row in rf:
            find = formats.find_ticket(row)
            for i in find:
                repeated = formats.check_list_csv_repeated("teste.csv")
                array = np.asarray_chkfinite(i)
                for r in repeated:
                    if r == i:
                        row = row.replace("not_repeated", "repeated")
            te = formats.remove_ticket(row)
            if not te.startswith("id"):
                new_array = [
                    int(te.split(",")[0]),
                    [int(x) for x in list(array)],
                    te.split(",")[2],
                    te.split(",")[3],
                    te.split(",")[4],
                    te.split(",")[5].strip(),
                ]
            else:
                new_array = [
                    te.split(",")[0],
                    te.split(",")[1],
                    te.split(",")[2],
                    te.split(",")[3],
                    te.split(",")[4],
                    te.split(",")[5].strip(),
                ]
            temp.append(new_array)
    rf.close()
    with open(formats.path_database("teste.csv"), "w") as wf:
        writer = csv.writer(wf)
        writer.writerows(temp)
    wf.close()
    print("Done...")


def classification():
    base = pd.read_csv(formats.path_database("teste.csv"))

    print(base.loc[base.repeated == "repeated"])

    previsores = base.iloc[:, 1:5].values
    classe = base.iloc[:, 5].values

    encoder_previsores = LabelEncoder()
    previsores[:, 0] = encoder_previsores.fit_transform(previsores[:, 0])
    previsores[:, 1] = encoder_previsores.fit_transform(previsores[:, 1])
    previsores[:, 2] = encoder_previsores.fit_transform(previsores[:, 2])
    previsores[:, 3] = encoder_previsores.fit_transform(previsores[:, 3])

    # encoder_classe = LabelEncoder()
    # classe = encoder_classe.fit_transform(classe)

    # converter variaveis do tipo categorico nominal em numbers - dump
    # onehotencoder = OneHotEncoder(categories="auto", sparse=False)
    # previsores = onehotencoder.fit_transform(previsores)

    # scaler = StandardScaler()
    # previsores = scaler.fit_transform(previsores)

    (
        previsores_treinamento,
        previsores_teste,
        classe_treinamento,
        classe_teste,
    ) = train_test_split(previsores, classe, test_size=0.25, random_state=0)

    # formats.debug(
    #     size_total=len(previsores),
    #     size_treinamento=len(previsores_treinamento),
    #     size_test=len(previsores_test),
    # )

    classificador = GaussianNB()
    classificador = classificador.fit(previsores, classe)
    previsoes = classificador.predict(previsores_teste)
    precisao = accuracy_score(classe_teste, previsoes)
    matriz = confusion_matrix(classe_teste, previsoes)

    # debug(previsores=previsores[:, 0:3])
    # print(pd.DataFrame(previsores))
    # print(formats.convert_csv_to_json(formats.path_database("teste.csv")))

    # print(pd.DataFrame(previsoes))


def numbersMostRepeated():
    matrix = list()
    with open(formats.path_database("teste.csv"), "r") as rfile:
        for row in rfile:
            numExtracted = formats.find_ticket(row)
            for i in numExtracted:
                arr = [int(x) for x in list(np.asarray_chkfinite(i))]
                matrix.append(arr)
    rfile.close()
    df = pd.DataFrame(matrix)
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    imputer = imputer.fit(df)
    df = imputer.transform(df)
    df = pd.DataFrame(df)
    for c in df.columns:
        columns = df[c].value_counts(normalize=False, sort=True, ascending=False).head(6)
        print([int(x) for x in list(columns.index)])


# area de chamadas das funções
# update_csv_file()
writeTickets(formats.create_payload_to_csv(100000))
# classification()
# numbersMostRepeated()