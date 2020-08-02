# -*- coding: utf-8 -*-
#! python3

"""
  Debugging
"""
import traceback
import os

market_2nd = {'ns': 'green', 'ew': 'red'}

def debugging(**Kwargs):
  for key, value in Kwargs.items():
    print("%s -> %s" %(key, value))


def handleErrors():
  try:
    raise Exception('This is the error message')
  except:
    errorFile = open('error_logs.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    debugging(error="The traceback info was written error_logs.txt")

def switchLights(intersection):
  for key in intersection.keys():
    if intersection[key] == 'green':
      intersection[key] = 'yellow'
    elif intersection[key] == 'yellow':
      intersection[key] = 'red'
    elif intersection[key] == 'red':
      intersection[key] = 'green'
  assert 'red' in intersection.values(), 'Neighter light is red' + str(intersection)


switchLights(market_2nd)
