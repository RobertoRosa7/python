# -*- coding: utf-8 -*-

"""

STRING METHOD
"""

text = 'This is a text'
text_list = ['cat', 'dog', 'bat']

text.lower()  # convert to text lowercase
text.upper()  # convert to text uppercase
text.islower()  # return boolean
text.isupper()  # return boolean
text.upper().isupper()  # statement valid
text.isalpha()  # letters only
text.isspace()  # whitespace only
text.istitle()  # titlecase only
text.isalnum()  # letters and numbers only
text.isdecimal()  # numbers only
text.startswith('this')  # return boolean - false because t is lowercase
text.startswith('This')  # return boolean - true because T is uppercase
text.endswith('text')  # return boolean

', '.join(text_list)  # join list to string
text.split()  # convert string to array
text.rjust(10)  # apply space to right and adding caracteres
text.rjust(10, '-')  # apply space to right
text.ljust(20)  # apply space to left
text.ljust(20, '*')  # apply space to left and adding caracteres
text.center(20)  # center text
text.strip()  # remove whitespace - not overwrite variable, need create new variable
text.rstrip()  # remove whitespace right side only
text.lstrip()  # remove whitespace left side only
text.strip('a')  # remove all occurrence
text.replace('e', 'a')  # replace all occurrence e for a


