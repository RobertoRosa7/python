# -*- coding: UTF-8 -*-
from datetime import date
class Item(object):
  def __init__(self, descricao, valor):
    self.__descricao = descricao
    self.__valor = valor

  @property
  def descricao(self):
    return self.__descricao
  
  @property
  def valor(self):
    return self.__valor

class Nota_fiscal(object):
  def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=[]):
    self.__razao_social = razao_social
    self.__cnpj = cnpj
    self.__data_de_emissao = data_de_emissao
    self.__itens = itens
    if len(detalhes) > 20:
      raise Exception('Detalhes da nota fiscal não pode ter mais que 20 caracteres')
    self.__detalhes = detalhes
    for observer in observadores:
      observer(self)

  @property
  def razao_social(self):
    return self.__razao_socail

  @property
  def cnpj(self):
    return self.__cnpj

  @property
  def data_de_emissao(self):
    return self.__data_de_emissao

  @property
  def detalhes(self):
    return self.__detalhes


if __name__ == '__main__':
  from observer import enviar_por_email, imprime, salvar_no_banco

  itens = [Item('Item A', 100), Item('Item B', 200)]
  nota_fiscal = Nota_fiscal(
      razao_social='FHSA Limitada', 
      cnpj='012345678901234', 
      itens=itens, 
      observadores=[imprime, enviar_por_email, salvar_no_banco])

  # nota_fiscal_com_builder = (Criador_nota_fiscal()
  #                           .com_razao_social('FHSA Limitada')
  #                           .com_cnpj('012345678901234')
  #                           .com_itens(itens)
  #                           .constroi())