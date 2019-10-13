# -*- coding: utf-8 -*-

'''
  Python Generators
  Fibonacci: 1,1,2,3,5,8....
  Funções Geradoras retornas geradores que são funções
'''

def fib(max):
  x, y = 1, 1
  while x < max:
    yield x
    x, y = y, x + y

gen = fib(10)
# print(gen) # sem uso do next()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for key in gen:
  print(key, end=' ')