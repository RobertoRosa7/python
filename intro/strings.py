# -*- coding: utf-8 -*-
from fnmatch import fnmatch, fnmatchcase
import re

def findMatch():
  '''
    Muito utilizado para URL's isso indica uma exata correspondência de caracteres
    o método match só verifica o início de uma string, e (r) é usado para strings simples
    que não há necessidade de usar barra invertida
  '''
  # print(fnmatch('arquivo.txt', '*.txt')) # return true
  # print(fnmatch('file.py', '*.txt')) # return false
  # print(fnmatch('arquivo0001.txt', 'arquivo[0-9]*')) # return true
  # print(fnmatch('arquivo002.png', '*.txt')) # return false
  # print(fnmatchcase('arq.txt', '*.TXT')) # return false

  # data = '06/11/2019'
  # url = 'https://'
  defaultPattern = re.compile(r'\d+/\d+/\d+')
  # response = True if re.match(r'\d+/\d+/\d+', url) else False
  # response = True if defaultPattern.match(url) else False
  # print(data, response)

  # find all occurrence
  texto = 'blablablabla, 11/12/2019, blablablablablabla, 01/01/2020'
  print(defaultPattern.findall(texto))

def strings():
    '''
        Manipulação de strings
    '''
    # substituir uma palavra da string
    texto = 'eu amo estudar javascript, mas no meu tempo livre estudo python'
    print(texto.replace('javascript', 'php'))

    texto02 = 'eu nasci na data de 26/02/1987 e minha irmã nasceu em 10/12/1980'
    print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', texto02))

    texto03 = 'eu nasci em 1987-02-26'
    print(re.sub(r'(\d+)-(\d+)-(\d+)', r'\3/\2/\1', texto03))

    # acessar cada caracter
    # nome = 'roberto'

    # substituir algum caracter por outro
    # nome = 'roberto'
    # lista = list(nome) # necessário para substituíção 
    # lista[0] = 't'
    # nome = ''.join(lista)

    # para saber o final de uma string | .txt | .png | .pdf | .zip etc...
    # file = 'arquivo.txt'
    # print(file.endswith('.txt')) # return boolean
    # print(file.startswith('arq')) # return boolean

strings()
def stringImutaveis():
  '''
    Strings in python são imutáveis por não poder receber atribuição de novos valores em suas
    
    string = python
    string[0] = 'a' error não é possível realizar esta instrução
  '''

  # não é possível
  # name = 'python'
  # name[0] = 'j'

  # jeito correto de alterar um caracter na sua posição
  name = 'python'
  name = 'J' + name[1:]

  print(name)