# -*- coding: UTF-8 -*-
class Contato:
  def __init__(self, id, nome, email):
    self.__id = id
    self.__nome = nome
    self.__email = email
  
  @property
  def id(self):
    return self.__id

  @property
  def nome(self):
    return self.__nome
  
  @property
  def email(self):
    return self.__email
  
  def set_id(self, id):
    self.__id = id
  
  def set_nome(self, nome):
    self.__nome = nome
  
  def set_email(self, email):
    self.__email = email