# -*- coding: utf-8 -*-

def strings():
    '''
        Manipulação de strings
    '''

    # acessar cada caracter
    # nome = 'roberto'

    # substituir algum caracter por outro
    nome = 'roberto'
    lista = list(nome) # necessário para substituíção 
    lista[0] = 't'
    nome = ''.join(lista)

    # para saber o final de uma string | .txt | .png | .pdf | .zip etc...
    file = 'arquivo.txt'
    # print(file.endswith('.txt')) # return boolean
    print(file.startswith('arq')) # return boolean

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