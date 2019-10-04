# -*- coding: utf-8 -*- 

class Pessoa:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return self.name

# critério de ordenação 
def byName(pessoa):
  return pessoa.name

def byAge(pessoa):
  return pessoa.age

p1 = Pessoa('João', 32)
p2 = Pessoa('Ana', 23)
p3 = Pessoa('Gabriel',28)
p4 = Pessoa('Sandra',18)

pessoas = [p1, p2, p3, p4]

# print(sorted(pessoas)) # error - falta critério de orndenação
print(sorted(pessoas, key = byAge))
print(sorted(pessoas, key = byAge, reverse=True))