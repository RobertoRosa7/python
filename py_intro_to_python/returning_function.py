# -*- coding: utf-8 -*-

def returningFunction(num):
  '''
    Retornando funções dentro de outras funções
  '''
  def child1():
    print("Hi! I'm son one")
  def child2():
    print("Hi! I'm son two")

  # checking conditional
  try:
    assert num == 20
    return child2
  except AssertionError:
    return child1

f1 = returningFunction(20)
f2 = returningFunction(10)

f1()
f2()
