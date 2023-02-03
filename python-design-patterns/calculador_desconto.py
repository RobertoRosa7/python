# -*- coding: UTF-8 -*-

from desconto import Desconto_por_cinto_itens, Desconto_por_mais_de_quinhento_reais,Sem_desconto

class Calculador_desconto(object):
  
  # chain of responsability
  def calcular(self, orcamento):
    desconto = Desconto_por_cinto_itens(
      Desconto_por_mais_de_quinhento_reais(Sem_desconto())
      ).calcula(orcamento)
    return desconto

if __name__ == '__main__':
  from orcamento import Orcamento, Item

  orcamento = Orcamento()
  orcamento.adiciona_item(Item('Item -1', 100))
  orcamento.adiciona_item(Item('Item -2', 50))
  orcamento.adiciona_item(Item('Item -3', 100))
  orcamento.adiciona_item(Item('Item -4', 100))
  orcamento.adiciona_item(Item('Item -5', 100))
  orcamento.adiciona_item(Item('Item -6', 100))

  calculador = Calculador_desconto()
  desconto = calculador.calcular(orcamento)

  print("Desconto calculado %.2f%%" % desconto)