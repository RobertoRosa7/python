# -*- coding: UTF-8 -*-
import csv, pickle, json
from operator import mod
from contato import Contato

def csv_para_contatos(caminho, encoding="latin_1"):
  contatos = []
  
  with open(caminho, encoding=encoding) as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
      id, nome, email = linha
      contato = Contato(id, nome, email)
      contatos.append(contato)
  return contatos

def contatos_para_pickle(contatos, caminho):
  with open(caminho, mode='wb') as arquivo:
    pickle.dump(contatos, arquivo)

def contatos_para_json(contatos, caminho):
  with open(caminho, mode='w') as arquivo:
    json.dump(contatos, arquivo)