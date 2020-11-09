# -*- coding: utf-8 -*-
import os, sys
import csv
import json


class Formats:
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
