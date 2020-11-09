# -*- coding: utf-8 -*-
import os, sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import csv
import json


class Formats:
    def path_database(self, filename):
        return os.path.join(os.path.dirname(__file__), "../databases/" + filename)
        # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        # print(os.path.abspath(os.path.join(os.path.dirname(__file__), 'databases')))