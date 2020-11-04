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


def otherWayToGenerateArray(n):
    arr = []
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


# df = pd.read_csv(os.path.join(os.getcwd(), 'databases/mega.csv'))

# with open(os.path.join(os.getcwd(), 'databases/mega.json'), 'r') as f:
#     t = json.loads(f.read())
#     teste = {'content': [0, 0, 0, 0, 0, 0],
#              'date': '2020-11-03', 'concurso': '2024', 'created_at': str(datetime.datetime.now())}

#     print('antes', len(t['mega']))
#     t['mega'].append(teste)
#     print('depois', len(t['mega']))
#     print(t['mega'][-1])
# f.close()

with open(os.path.join(os.getcwd(), 'databases/mega.csv'), 'r') as f:
    print(f.read())
    f.close()
