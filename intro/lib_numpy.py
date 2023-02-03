# -*- coding: utf-8 -*-
'''
  Biblioteca numpy usado para operações de calculos científicos
'''
import numpy as np

def default():
  x = np.array([1,2,3])
  y = np.array([4,5,6])

  # multiplicando os valores dentro do array 
  print(x * 2, 'x')

  # soma
  print(y + 2, 'y')

  # subtração
  print(y - 1, 'y')

  # raiz quadrada
  print(np.sqrt(x))

  # matrix
  print(np.matrix([[1,2], [3,4]]))
default()