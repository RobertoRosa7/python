# -*- coding: utf-8 -*-
import os, csv, json, re, datetime, math, random
import pandas as pd
import numpy as np
from flask import make_response


class Formats:
    """Formats

    Utils
    -----
    Para uso de recursos que podem ser utils
    """

    def debug(self, **Kwargs):
        """Debug: string"""
        for key, value in Kwargs.items():
            print("key %s, value %s" % (key, value))

    def path_database(self, filename):
        """
        Return : String
        Notes
        -----
          Retorna uma string com o path completo para o diretório databases

        """
        try:
            return os.path.join(os.path.dirname(__file__), "../databases/" + filename)
            # return os.path.abspath(
            #     os.path.join(
            #         os.path.dirname(os.getcwd()), "python/databases/" + filename
            #     )
            # )
        except FileNotFoundError:
            return "Arquivo ou Diretório não encontrado"

    def convert_csv_to_json(self, file_csv):
        """
        Parameter
        ---------
        file_csv : String, default=None

        Notes
        -----
        Converter um arquivo CSV para formato JSON, para uso do JavaScript em retorno API

        """
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
        arr.append(str(datetime.datetime.today().isoformat())[0:10])
        for i in range(n):
            arr.append(self.generateNumber(1, 60, np.empty(n), i))
        return arr

    def generateNumber(self, min=1, max=60, array=[], index=0):
        rand = math.ceil(random.randint(min, max))
        return self.generateNumber(min, max, array) if rand in array else rand

    def create_payload_model_mega(self, qtd, filename="mega.csv"):
        print("Start up...!")
        accumated = list()
        if not self.is_file_exists(filename):
            accumated.append(self.otherWayToGenerateArray(6))
            return accumated

        with open(self.path_database(filename), "rb") as readFile:
            lines = len(readFile.readlines())
            if lines > 1:
                for i in range(qtd):
                    accumated.append(self.otherWayToGenerateArray(6))
            else:
                accumated.append(self.otherWayToGenerateArray(6))
        readFile.close()
        return accumated

    def is_file_exists(self, filename):
        return os.path.exists(self.path_database(filename))

    def getPeriod(self, period, lastDate, firstDate):
        yearLastDate = int(lastDate.split("-")[0]) + period
        yearFirstDate = int(firstDate.split("-")[0]) - period

        dateMediaLast = (
            str(yearLastDate)
            + "-"
            + str(lastDate.split("-")[1])
            + "-"
            + str(lastDate.split("-")[2])
        )

        dateMediaFirst = (
            str(yearFirstDate)
            + "-"
            + str(firstDate.split("-")[1])
            + "-"
            + str(firstDate.split("-")[2])
        )
        return {"dateMediaLast": dateMediaLast, "dateMediaFirst": dateMediaFirst}
