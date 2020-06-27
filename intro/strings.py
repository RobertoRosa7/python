# -*- coding: utf-8 -*-
from fnmatch import fnmatch, fnmatchcase
import re

firstname = 'Roberto'
lastname = 'Rosa'
country = 'Brazil'
age = 33


def find_match():
  """
  Muito utilizado para URL's isso indica uma exata correspondência de caracteres
  o método match só verifica o início de uma string, e (r) é usado para strings simples
  que não há necessidade de usar barra invertida

  print(fnmatch('arquivo.txt', '*.txt')) return true
  print(fnmatch('file.py', '*.txt')) return false
  print(fnmatch('arquivo0001.txt', 'arquivo[0-9]*')) return true
  print(fnmatch('arquivo002.png', '*.txt')) return false
  print(fnmatchcase('arq.txt', '*.TXT')) return false
  """
  url = 'https://'
  default_pattern = re.compile(r'\d+/\d+/\d+')  # default pattern
  match_data = re.compile(r'\d+/\d+/d+\d+')  # data = '06/11/2019'
  match_url = default_pattern.match(url)  # url = 'https://'

  response = True if re.match(r'\d+/\d+/\d+', url) else False
  response = True if default_pattern.match(url) else False

  texto = 'blablablabla, 11/12/2019, blablablablablabla, 01/01/2020'
  print(default_pattern.findall(texto))  # find all occurrence


def strings():
  """
  Manipulação de strings
  acessar cada caracter
  nome = 'roberto'
  substituir algum caracter por outro
  nome = 'roberto'
  lista = list(nome) necessário para substituíção
  lista[0] = 't'
  nome = ''.join(lista)
  para saber o final de uma string | .txt | .png | .pdf | .zip etc...
  file = 'arquivo.txt'
  print(file.endswith('.txt')) return boolean
  print(file.startswith('arq')) return boolean
  """

  texto = 'eu amo estudar javascript, mas no meu tempo livre estudo python'
  print(texto.replace('javascript', 'php'))  # substituir uma palavra da string

  texto02 = 'eu nasci na data de 26/02/1987 e minha irmã nasceu em 10/12/1980'
  print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', texto02))  # substituir um padrão dentro da string
  print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', texto02, flags=re.IGNORECASE))  # ignorar case sensitive

  texto03 = 'eu nasci em 1987-02-26'
  print(re.sub(r'(\d+)-(\d+)-(\d+)', r'\3/\2/\1', texto03))

  texto04 = '      python    '
  print(texto04.strip())  # remover espaço em branco

  texto05 = '----------javascript---------'
  print(texto05.strip('-'))  # remover caracteres repetidos no inicio

  texto06 = '------------php'
  print(texto06.lstrip('-'))  # remover apenas do lado esquerdo

  texto07 = 'mysql----------'
  print(texto07.rstrip('-'))  # remover apenas do lado direito


def string_imutaveis():
  """
  Strings in python são imutáveis por não poder receber atribuição de novos valores em suas
  string = python
  string[0] = 'a' error não é possível realizar esta instrução
  """
  name = 'python'
  name = 'J' + name[1:]
  print(name)


def raw_string():
  """
  raw string only r, usado para tratar texto puro, sem nenhuma formatação de caracteres especiais
  """

  print(r'Isso é um texto\'s usando raw string')  # raw string
  print("Isso é um texto's usando aspas duplas e simples")  # aspas duplas
  print('Isso é um texto\'s usando barra escape') # barra escape


def format_string():
  print('Hello %s do you where from %s and your age is %s?' % (firstname, country, age))


format_string()
