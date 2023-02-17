#-*- coding: UTF-8 -*-
import csv, sys, os

sys.path.append(os.path.abspath(os.getcwd()))
# print()

def carregar_acessos():
  x = []
  y = []

  # path = os.getcwd() + '/py_classification/py_data/acesso.csv'
  with open('py_data/acesso.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    leitor.__next__()
    for home, como_funciona, contato, comprou in leitor:
      x.append([int(home), int(como_funciona), int(contato)])
      y.append(int(comprou))
  return x, y


def carregar_buscas():
  x = []
  y = []

  with open('py_data/busca.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    leitor.__next__()
    for home, busca, logado,comprou in leitor:
      x.append([int(home), busca, int(logado)])
      y.append(int(comprou))
  return x, y