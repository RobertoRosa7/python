# -*- coding: utf-8 -*-
#! python3

import os

"""
Walking Folders

listDir: os.walk(src_path)
"""

def debug(**Kwargs):
  for key, value in Kwargs.items():
    print("%s -> %s" %(key, value))


for foldername, subfolders, filename in os.walk(os.path.join(os.getcwd())):
  print('The folder is: ' + foldername)
  print('The subfolder in ' + foldername + ' are: ' + str(subfolders))
  print('The filename in ' + foldername + ' are: ' + str(filename))
  print()