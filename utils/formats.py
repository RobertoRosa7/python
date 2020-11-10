# -*- coding: utf-8 -*-
import os, csv, json, re, datetime, math, random
import pandas as pd
import numpy as np
from flask import make_response


class Formats:
    def debug(self, **Kwargs):
        for key, value in Kwargs.items():
            print("key %s, value %s" % (key, value))

    def path_database(self, filename):
        return os.path.join(os.path.dirname(__file__), "../databases/" + filename)

    def convert_csv_to_json(self, file_csv):
        json_file = {}

        with open(file_csv) as read_file:
            reader = csv.DictReader(read_file)
            for i, row in enumerate(reader):
                json_file[i] = row
        read_file.close()
        return json_file

    def json_response(self, obj, status_code=200, cls=None):
        response = make_response(json.dumps(obj, cls=cls), status_code)
        response.content_type = "application/json"
        return response

    def check_list_csv_repeated(self, filepath):
        if not filepath:
            return []
        list_repeated = list()
        with open(self.path_database(filepath)) as rf:
            temp = list()
            for row in rf:
                find = self.find_ticket(row)
                for i in find:
                    temp.append(i)

            list_repeated = pd.Series(temp)[pd.Series(temp).duplicated()].values
        rf.close()
        return list_repeated

    def find_ticket(self, text):
        return re.compile(
            r"(\d{2}|\d{1}),\s(\d{2}|\d{1}),\s(\d{2}|\d{1}),\s(\d{2}|\d{1}),\s(\d{2}|\d{1}),\s(\d{2}|\d{1})"
        ).findall(text)

    def remove_ticket(self, string):
        return re.sub(
            r"(\d{2}|\d{1}),\s(\d{2}|\d{1}),\s(\d{2}|\d{1}),\s(\d{2}|\d{1}),\s(\d{2}|\d{1}),\s(\d{2}|\d{1})",
            "",
            string,
        )

    def otherWayToGenerateArray(self, n):
        arr = list()
        for i in range(n):
            arr.append(self.generateNumber(1, 60, np.empty(n), i))
        return arr

    def generateNumber(self, min=1, max=60, array=[], index=0):
        rand = math.ceil(random.randint(min, max))
        return self.generateNumber(min, max, array) if rand in array else rand

    def create_payload_to_csv(self, qtd, filename="teste.csv"):
        accumulated = list()
        with open(self.path_database(filename), "rb") as readFile:
            lines = len(readFile.readlines())
            if lines > 1:
                for i in range(qtd):
                    lines += 1
                    accumulated.append(
                        [
                            lines,
                            self.otherWayToGenerateArray(6),
                            "2020-11-05",
                            "2024",
                            str(datetime.datetime.now()),
                            "not_repeated",
                        ]
                    )
            else:
                accumulated.append(
                    [
                        lines,
                        self.otherWayToGenerateArray(6),
                        "2020-11-05",
                        "2024",
                        str(datetime.datetime.now()),
                        "not_repeated",
                    ]
                )
        readFile.close()
        return accumulated