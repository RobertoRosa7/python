# -*- coding: utf-8 -*-

import csv
import json
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Formats:
    def path_databases(filename):
        return os.path.join(os.path.dirname(__file__), "databases/" + filename)
        # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        # print(os.path.abspath(os.path.join(os.path.dirname(__file__), 'databases')))
