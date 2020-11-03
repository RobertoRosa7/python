# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import random
import math

payload = {}


def otherWayToGenerateArray(n):
    arr = []
    for i in range(n):
        arr.append(generateNumber(1, 60, np.empty(n), i))
    return arr


def generateNumber(min=1, max=60, array=[], index=0):
    rand = math.ceil(random.randint(min, max))
    return generateNumber(min, max, array) if rand in array else rand


payload['ticker'] = otherWayToGenerateArray(6)

print(payload)
