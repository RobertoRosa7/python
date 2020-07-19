# -*- coding: utf-8 -*-
#! python3

import shutil
import os
import send2trash


"""
Moving and Copying

to copy:        shutil.copy(src_path, dist_path)
to copy folder: shutil.copytree(src_path, dist_path)
to move:        shutil.move(src_path, dist_path)
to rename:      shutil.move(src_path, dist_path)
to del file:    os.unlink(src_path)
to del folder:  os.rmdir(src_path) # empty
to del folder:  shutil.rmtree(src_path) # with content
"""

def debug(**Kwargs):
  for key, value in Kwargs.items():
    print("%s -> %s" %(key, value))

debug(currentDir=os.getcwd())  # /home/mendoza/Documentos/udemy/python
# shutil.copy(os.path.join(os.getcwd(), 'intro/arquivo_teste.txt'), os.path.join(os.getcwd()))  # copy file
# shutil.copytree(os.path.join(os.getcwd(), 'intro/teste_folder'), os.path.join(os.getcwd(), 'teste_folder_back'))  # copy folder
# shutil.move(os.path.join(os.getcwd(), 'intro/arquivo_teste.txt'), os.getcwd())  # move file and folder
shutil.move(os.path.join(os.getcwd(), 'intro/arquivo_teste2.txt'), os.path.join(os.getcwd(), 'intro/arquivo_teste.txt'))  # rename


# delete all file in folder
def del_files(path):
  os.chdir(os.path.join(os.getcwd(), path))

  for filename in os.listdir():
    if filename.endswith('.txt'):
      # os.unlink(filename)  # delete
      # send2trash.send2trash(filename)  # send to trash - recicle
      debug(file=filename)
  
  debug(totalFile=len(os.listdir()))