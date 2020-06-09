# -*- coding: utf-8 -*-

# def dividePorDois(dois):
#   # usando try and execpt trata do error mas não interrompe a execução do script
#   try:
#     return 32 / dois
#   except ZeroDivisionError:
#     print('Error: you tried to divide by zero')

# print(dividePorDois(2))
# print(dividePorDois(12))
# print(dividePorDois(0))
# print(dividePorDois(0))
# print(dividePorDois(3))


# Quanto gatos vc tem?
print('How many cats do you have?')
numCats = input()
try:
  if int(numCats) >= 4:
    print('That is a lot cats')
  else:
    print('That is not a lot cats')
except ValueError:
  print('Not a number')