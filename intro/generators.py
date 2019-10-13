# -*- coding: utf-8 -*-

def deco(func):
  '''
    Python Decorators:
    é uma função que recebe outra função como parâmetro, gera uma nova função que 
    que adiciona algumas funcionalidades á função original e retorna essa nova função.

    basicamente - é uma parâmetro que adiciona novas funcionalidades a função original sem
    passado como argumento.

    Normalmente usa @decorator
  '''

  # função de retorno
  def sub(a, b):
    return a - b
  
  def mult(a, b):
    return a * b

  # se pelo menos um dos números for par
  def somar(a, b):
    if a % 2 == 0 or b % 2 == 0:
      return a + b
    return a - b

  # qual será a função que será retornada
  # return sub
  return somar

@deco
def somar(a, b):
  return a + b

print(somar(5, 3))
def fib(max):
  '''
    Python Generators
    Fibonacci: 1,1,2,3,5,8....
    Funções Geradoras retornas geradores que são funções - funciona como um return
    porem é um generators
  '''
  x, y = 1, 1
  while x < max:
    yield x
    x, y = y, x + y

def execFib():

  # recebe o retorno de fibonacci
  gen = fib(10)

  # print(gen) # sem uso do next()
  # print(next(gen))
  # print(next(gen))
  # print(next(gen))
  # print(next(gen))
  # print(next(gen))
  # print(next(gen))

  # método mais simples
  for key in gen:
    print(key, end=' ')