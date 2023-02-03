import os, sys
sys.path.append(os.path.abspath(os.path.join('...')))

from utils.utils import Utils
import nltk


class Corretor(Utils):
  lista_normalizada = []
  total_palavras = 0

  def __init__(self):
    pass
  
  def set_total_palavras(self, total):
    self.total_palavras = total


  def get_total_palavras(self):
    return self.total_palavras


  def set_lista_normalizada(self, lista_palavras):
    self.lista_normalizada = lista_palavras


  def get_lista_normalizada(self):
    return self.lista_normalizada
  

  def openFile(self, path):
    file = None
    with open(path, 'r', encoding="utf-8") as f:
      file = f.read()
      f.close()
    return file

  
  def tokenization(self, text:str):
    return nltk.tokenize.word_tokenize(text)
  
  
  def separa_palavras(self, lista_tokens:list):
    lista_palavras = []
    for token in lista_tokens:
      if token.isalpha():
        lista_palavras.append(self.normalizacao_tolower(token))

    self.set_lista_normalizada(lista_palavras)
    self.set_total_palavras(len(lista_palavras))
    return lista_palavras

  
  def normalizacao_tolower(self, palavra:str):
    return palavra.lower()


  def gerador_palavras(self, palavra:str):
    fatias = []
    for i in range(len(palavra) + 1):
      fatias.append((palavra[:i], palavra[i:]))
    palavras_gerada = self.insere_letras(fatias)
    return palavras_gerada


  def insere_letras(self, fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for lado_esquerdo, lado_direito in fatias:
      for letra in letras:
        novas_palavras.append(lado_esquerdo + letra + lado_direito)
    return novas_palavras
  

  def corretor(self, palavra:str):
    palavra_geradas = self.gerador_palavras(palavra)
    palavra_correta = max(palavra_geradas, key=self.probabilidade)
    return palavra_correta
  

  def probabilidade(self, palavra_gerada):
    # para calcular a probabilidade é necessário 
    # ter a frequência e também ter o total
    # então a probabilidade será a freq dividido pelo total
    # prob = freq / total

    frequencia = nltk.FreqDist(self.get_lista_normalizada())
    return frequencia[palavra_gerada] / self.get_total_palavras()


  def avaliador(self, testes):
    numero_palavras = len(testes)
    acertou = 0
    for correta, errada in testes:
      palavra_corrigida = self.corretor(errada)
      if palavra_corrigida == correta:
        acertou += 1
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)

    print(f"Taxa de acerto {taxa_acerto}% de {numero_palavras} palavras")

  
  def cria_dados_testes(self, path):
    lista_palavras_teste = []
    file = open(path, 'r', encoding="utf-8")

    for linha in file:
      correta, errada = linha.split()
      lista_palavras_teste.append((correta, errada))
    file.close()
    return lista_palavras_teste