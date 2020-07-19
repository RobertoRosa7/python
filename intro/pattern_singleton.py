# -*- coding: utf-8 -*-

# Permite somente uma instancia
class Singleton(object):
  def __new__(cls):
    # verifica se já existe uma instância desta classe
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton, cls).__new__(cls)
    return cls.instance


# Lazy instance - instancia preguiçosa
class LazySingleton(object):
  __instance = None
  def __init__(self):
    if not LazySingleton.__instance:
      print('__init__ foi chamado')
    else:
      print('instancia já foi criada', self.getInstance())
  
  @classmethod
  def getInstance(cls):
    if not cls.__instance:
      cls.__instance = LazySingleton()
    return cls.__instance

s1 = LazySingleton()
print('Objeto criado: ', LazySingleton.getInstance())
s2 = LazySingleton()
