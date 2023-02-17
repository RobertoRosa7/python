import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


class Utils:
  def __init__(self):
    pass
  
  def plotar(self, x, y, data, title='', xLabel='', yLabel=''):
    sns.set_palette('Accent')
    sns.set_style('darkgrid')
    ax = sns.lineplot(x=x, y=y, data=data)
    ax.figure.set_size_inches(14,5)
    ax.set_title(title, loc='left', fontsize=18)
    ax.set_xlabel(xLabel, fontsize=14)
    ax.set_ylabel(yLabel, fontsize=14)
    ax = ax
    return x


  def plot_comparacao(self, x, y1, y2, y3, dataset, title):
    plt.figure(figsize=(16,12))
    ax = plt.subplot(3, 1,1)
    ax.set_title(title, fontsize=18, loc='left')
    sns.lineplot(x=x, y=y1, data=dataset)
    plt.subplot(3,1,2)
    sns.lineplot(x=x, y=y2, data=dataset)
    plt.subplot(3,1,3)
    sns.lineplot(x=x, y=y3, data=dataset)
    ax = ax
    return ax


  def show_line_and_columns(self, dataframe):
    print("Quantidade de linhas e colunas {}".format(dataframe.shape))
  

  def show_data_none(self, dataframe):
    print("Quantidade de dados nulos {}".format(dataframe.isna().sum().sum()))
  
  def buscar_media_movel(self, series:pd.Series, dias:int):
    return series.rolling(dias).mean()