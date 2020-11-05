# -*- coding: utf-8 -*-
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import datetime
import random
import math
import os
import json
import csv

payload = {}
accumulated = list()


def path_database(file):
    return os.path.join(os.getcwd(), "databases/" + file)


def otherWayToGenerateArray(n):
    arr = list()
    for i in range(n):
        arr.append(generateNumber(1, 60, np.empty(n), i))
    return arr


def generateNumber(min=1, max=60, array=[], index=0):
    rand = math.ceil(random.randint(min, max))
    return generateNumber(min, max, array) if rand in array else rand


def converte_json_to_csv():
    # dcsv = pd.read_csv(os.path.join(os.getcwd(), 'databases/mega.csv'))
    # djson = pd.read_json(os.path.join(os.getcwd(), 'databases/mega.json'))
    # dataCsv = dataJson.to_csv(os.path.join(os.getcwd(), 'databases/mega.csv'), index=None)

    with open(path_database("mega.json"), "r") as f:
        to_python = json.loads(f.read())
        with open(path_database("mega.csv"), "w") as fcsv:
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
    with open(path_database("mega.csv"), "r") as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == str(id_line):
                    lines.remove(row)
    readFile.close()

    with open(path_database("mega.csv"), "w") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    writeFile.close()


def writeTickets(payload_csv):
    with open(path_database("teste.csv"), "rb") as readFile:
        lines = len(readFile.readlines())
        with open(path_database("teste.csv"), "a") as writeFile:
            writer = csv.writer(writeFile)
            if lines > 0:
                for row in payload_csv:
                    writer.writerow(row)
            else:
                writer.writerow(["id", "ticket", "date", "concurso", "created_at"])
                for row in payload_csv:
                    writer.writerow(row)

        writeFile.close()
    readFile.close()


def create_csv():
    with open(path_database("teste.csv"), "rb") as readFile:
        lines = len(readFile.readlines())
        if lines > 1:
            for i in range(10):
                lines += 1
                accumulated.append(
                    [
                        lines,
                        otherWayToGenerateArray(6),
                        "2020-11-05",
                        "2024",
                        str(datetime.datetime.now()),
                    ]
                )
        else:
            accumulated.append(
                [
                    lines,
                    otherWayToGenerateArray(6),
                    "2020-11-05",
                    "2024",
                    str(datetime.datetime.now()),
                ]
            )
    readFile.close()


# create_csv()
# print(accumulated)
base = pd.read_csv(path_database("teste.csv"))
previsores = base.iloc[:, 1:5].values
encoder_previsores = LabelEncoder()
previsores[:, 0] = encoder_previsores.fit_transform(previsores[:, 0])
previsores[:, 1] = encoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 2] = encoder_previsores.fit_transform(previsores[:, 2])
previsores[:, 3] = encoder_previsores.fit_transform(previsores[:, 3])

onehotencoder = OneHotEncoder(categories='auto', sparse=False)
previsores = onehotencoder.fit_transform(previsores)

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
# locate = base.loc[base.ticket]
# writeTickets(accumulated)
print(previsores)
