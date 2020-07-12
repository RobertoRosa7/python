# -*- coding: utf-8 -*-
import os

"""
  Windows: c:\
  Linux/Mac: /
  Using for windows: print('c:\\folder\\file.png') or print(r'c:\folder\file.png')
"""

def debug(**Kwargs):
  for key, value in Kwargs.items():
    print("%s -> %s" %(key, value))

create_path = os.path.join('folder1', 'folder2', 'folder3', 'file.png')  # create a path
current_path = os.getcwd() # the current path directory
identify_dash = os.sep  # identify dash from sistem operator
absolute_path = os.path.abspath('file.py')  # /home/mendoza/Documentos/udemy/python/file.py
parent_path = os.path.abspath('../../file.py')  # /home/mendoza/Documentos/file.py
is_abspath = os.path.isabs('../../file')  # return false
dirname_path = os.path.dirname('/home/mendoza/Documentos/udemy/python/file.py')  # /home/mendoza/Documentos/udemy/python
basename_path = os.path.basename('/home/mendoza/Documentos/udemy/python/file.py')  # file.py
exists_path = os.path.exists('/home/mendoza/Documentos/udemy/python/file.py')  # false
exists_path2 = os.path.exists('/home/mendoza/Documentos/udemy/python')  # true
is_dir = os.path.isdir('/home/mendoza/Documentos/udemy/python')  # true
is_file = os.path.isfile('/home/mendoza/Documentos/udemy/python/filename_filepath/filename_filepath.py')  # true
size_file = os.path.getsize('/home/mendoza/Documentos/udemy/python/filename_filepath/filename_filepath.py') # size
ls_dir = os.listdir('/home/mendoza/Documentos/udemy/python') # list dir
# os.makedirs('/dirname') # create new directory
# os.chdir('/') # change directory to root
# DELETE_THIS_FILE('filename.png')  # delete file


def get_total_size():
  total_size = 0
  dir_path = '/home/mendoza/Documentos/udemy/python/intro'
  for filename in os.listdir(dir_path):
    if not os.path.isfile(os.path.join(dir_path, filename)):
      continue
  total_size += os.path.getsize(os.path.join(dir_path, filename))
  debug(totalSize=total_size)


debug(path=current_path)