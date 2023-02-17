# -*- coding: utf-8 -*-
from validate_docbr import CPF, CNPJ

doc = '36212891869'
# doc = '34.740.751/0001-66'
print(len(doc))

class Document:
  @staticmethod
  def create_document(document):
    if len(document) == 11:
      return DoCpf(document)
    elif len(document) == 14 or len(document) == 18:
      return DoCnpj(document)
    else:
      raise ValueError('Quantidade de digitos inválidos.')

class DoCnpj:
  def __init__(self, document):
    if self.cnpj_is_valid(document):
      self.cnpj = document
    else:
      raise ValueError('CNPJ inválido')

  def cnpj_is_valid(self, cnpj):
      validator_cnpj = CNPJ()
      return validator_cnpj.validate(cnpj)
  
  def format_cnpj(self):
    mascara = CNPJ()
    return mascara.mask(self.cnpj)

  def __str__(self):
    return self.format_cnpj()


class DoCpf:
  def __init__(self, document):
    if self.cpf_is_valid(document):
      self.cpf = document
    else:
      raise ValueError('CPF inválido')

  def __str__(self):
     return self.format_cpf()

  def cpf_is_valid(self, document):
    validador = CPF()
    return validador.validate(document)

  def format_cpf(self):
    mascara = CPF()
    return mascara.mask(self.cpf)
  

document = Document.create_document(doc)
print(document)