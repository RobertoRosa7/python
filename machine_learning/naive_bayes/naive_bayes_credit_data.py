# -*- coding: utf-8 -*-
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import os


def path_databases(filename):
    return os.path.join(os.getcwd(), "databases/" + filename)


# importando arquivo pra leitura
base = pd.read_csv(path_databases("credit_data.csv"))

# tratando valores menores que zero e aplicando idade média
base.loc[base.age < 0, "age"] = 40.92  # base.age[base.age > 0].mean())

# separando previsores e classe
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4]

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(previsores[:, 1:4])

# tratando de campos null
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

scaler = StandardScaler()
# tratando padronização
previsores = scaler.fit_transform(previsores)

print(pd.DataFrame(previsores))