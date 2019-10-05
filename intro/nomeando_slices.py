# -*- coding: utf-8 -*-

def namedSlice():
  '''
    Nomeando slices: struct slice(start, end, step)
  '''
  lista = [2,2,34,5,24,1,3]
  theLastTree = slice(-3, None)

  print(lista[theLastTree])

namedSlice()