# -*- coding: utf-8 -*-

class Complex:
  def __init__(self, r, i):
    self.r = r
    self.i = i

  # mostrar de forma mais legível
  def __repr__(self):
    return '({0},{1}i)'.format(self.r, self.i)

  # adicionand metodo especial
  def __add__(self, others):
    return Complex(self.r + others.r, self.i + others.i)

num = Complex(3,1)
num2 = Complex(2,4)
num3 = num + num2
print(num3)