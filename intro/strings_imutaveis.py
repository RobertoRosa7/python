# -*- coding: utf-8 -*-

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

stringImutaveis()