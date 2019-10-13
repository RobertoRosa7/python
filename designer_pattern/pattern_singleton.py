# -*- coding: utf-8 -*-

# Permite somente uma instancia
class Singleton(object):
  def __new__(cls):
    # verifica se já existe uma instância desta classe
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton, cls).__new__(cls)
    return cls.instance

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)