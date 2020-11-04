# -*- coding: utf-8 -*-

import pandas as pd
import os

base = pd.read_csv(os.path.join(
    os.getcwd(), 'databases/credit_data.csv'))
print(base.describe())


# base - mostra a tabela de dados - DataFrame
# base.describe() - faz uma prévia análise descrevendo com porcentagem
