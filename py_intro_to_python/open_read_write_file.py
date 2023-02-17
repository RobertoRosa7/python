# -*- coding: utf-8 -*-
import os
import shutil

"""
Open, Read and Write files
Trabalhando com arquivos:
    Abrir:
    open(nome, modo)
    modo:
        r: somente leitura
        w: gravação, gera novo arquivo vazio, sobreescreve existentes
        a: leitura e escrita, adiciona novo conteúdo no fim do arquivo
        r+: leitura e escrita
        w+: escrita
        a+: leitura e escrita - abre o arquivo para atualização

    Ler:
    read() - lê arquivo inteiro
    readline() - lê apenas uma linha
    readelines() - lê o arquivo e gera nova lista (array)
"""

def debug(**Kwargs):
  for key, value in Kwargs.items():
    print("%s -> %s" %(key, value))


def read():
  with open('/home/mendoza/Documentos/udemy/python/py_intro_to_python/arquivo_teste.txt', 'r') as f:
    # debug(read=f.read())  # read
    # debug(readline=f.readline())  # readline single
    debug(readline=f.readlines())  # readlines lists
    f.close()


def writeFile():
  
  with open(os.path.join(os.getcwd(), 'arquivo_teste3.txt'), 'w') as f:
    f.write('This file was writen by python')
    f.close()
  
  with open(os.path.join(os.getcwd(), 'arquivo_teste3.txt'), 'r') as f:
    debug(read=f.read())
    f.close()


def copying():
  shutil.copy(
    os.path.join(os.getcwd(), 'arquivo_teste3.txt'), 
    os.path.join(os.path.abspath('../../'), 'arquivo_teste3.txt')
  ) # Files

  shutil.copytree(
    os.path.join(os.getcwd(), 'teste_folder'),
    os.path.join(os.path.abspath('../../'), 'teste_folder_back')
  ) # Folders

# copying()