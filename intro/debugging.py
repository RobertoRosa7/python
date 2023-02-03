# -*- coding: utf-8 -*-
#! python3


"""
  Debugging
"""


import traceback
import os
import logging


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # stdout
logging.basicConfig(filename='python_logs.txt', format='%(asctime)s - %(levelname)s - %(message)s')  # file

# logging.disable(logging.CRITICAL)
# logging.disable(logging.INFO)
# logging.disable(logging.WARNING)
# logging.disable(logging.ERROR)

# logging.debug()
# logging.info()
# logging.warning()
# logging.critical()
# logging.error()

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


logging.debug('Start debugging')


def fatorial(n):
  logging.info('debugging of fatoria(%s)' %(n))
  total = 1
  for i in range(1, n + 1):
    total *= i
    logging.info('i is %s, total is %s' %(i, total))
  
  logging.debug('return value is %s' %(total))
  return total


debugging(fatorial=fatorial(5))
logging.debug('End debugging')