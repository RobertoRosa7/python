# -*- coding: utf-8 -*-
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


def pathDatabase(file):
    return os.path.join(os.getcwd(), 'databases/' + file)


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

    with open(os.path.join(os.getcwd(), 'databases/mega.json'), 'r') as f:
        to_python = json.loads(f.read())
        with open(os.path.join(os.getcwd(), 'databases/mega.csv'), 'w') as fcsv:
            fs = csv.writer(fcsv)
            fs.writerow(['id', 'ticket', 'date', 'concurso', 'created_at'])
            for i, data in enumerate(to_python['mega']):
                fs.writerow(
                    [
                        i,
                        data['content'],
                        data['date'],
                        data['concurso'],
                        data['create_at']
                    ]
                )
        fcsv.close()
    f.close()


def removeLines(id_line):
    lines = list()
    with open(pathDatabase('mega.csv'), 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == str(id_line):
                    lines.remove(row)
    readFile.close()

    with open(pathDatabase('mega.csv'), 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    writeFile.close()


def writeTickets(payload_csv):
    with open(pathDatabase('teste.csv'), 'rb') as readFile:
        lines = len(readFile.readlines())
        with open(pathDatabase('teste.csv'), 'a') as writeFile:
            writer = csv.writer(writeFile)
            if lines > 0:
                for row in payload_csv:
                    writer.writerow(row)
            else:
                writer.writerow(
                    ['id', 'ticket', 'date', 'concurso', 'created_at'])
                for row in payload_csv:
                    writer.writerow(row)

        writeFile.close()
    readFile.close()


# for i in range(100000):
#     accumulated.append([i, otherWayToGenerateArray(
#         6), '2024', str(datetime.datetime.now())])

base = pd.read_csv(pathDatabase('teste.csv'))
# locate = base.loc[base.ticket == base.ticket]

# print(locate)
