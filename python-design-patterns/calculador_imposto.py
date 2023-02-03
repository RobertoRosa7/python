# -*- coding: UTF-8 -*-
from impostos import ICMS, ISS,ICPP,IKCV

class Calculador_impostos(object):
  def realiza_calculo(self, orcamento, imposto):
    imposto_calculado = imposto.calcula(orcamento)
    print(imposto_calculado)


if __name__ == '__main__':
  from orcamento import Orcamento, Item

  calculador = Calculador_impostos()
  orcamento = Orcamento()
  
  orcamento.adiciona_item(Item('1', 50))
  orcamento.adiciona_item(Item('2', 200))
  orcamento.adiciona_item(Item('3', 250))
  print('Descontos\n')

  calculador.realiza_calculo(orcamento, ISS())
  calculador.realiza_calculo(orcamento, ICMS())
  print('Impostos: ISS e ICMS\n')

  calculador.realiza_calculo(orcamento, ICPP())
  calculador.realiza_calculo(orcamento, IKCV())
  print('Impostos: ICPP e IKVC\n')

  calculador.realiza_calculo(orcamento, ISS(ICMS()))
  calculador.realiza_calculo(orcamento, ICPP(IKCV()))
  print('Imposto composto:\n')