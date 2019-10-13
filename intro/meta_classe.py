# -*- coding: utf-8 -*-

class MinhaMetaClass(type):
  def __new__(cls, clsname, superclasses, attributedict):
    print('clsname', clsname)
    print('superclasses', superclasses)
    print('atributos', attributedict)
    return type.__new__(cls, clsname, superclasses, attributedict)

class Pai(): pass
class Filha(Pai, metaclass=MinhaMetaClass): pass

obj = Filha()
print(obj.__class__.__class__)