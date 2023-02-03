# -*- coding: utf-8 -*-

import pprint

# DICTIONARIES DATA TYPE IS REPRESENT BY {}
my_cat = {'name': 'tom', 'age': 5, 'color': 'gray and white', 'disposition': 'loud'}
dic_dif = {1: 'num_one', 2: 'num_two', 3: 'num_three'}

# FIND KEY IN DICTIONARY
print('find -> ', 'disposition' in my_cat)

# EXTRACT KEYS
print('keys -> ', list(dic_dif.keys()))

# EXTRACT VALUES
print('values -> ', list(my_cat.values()))

# EXTRACT ITEMS
print('items -> ', list(dic_dif.items()))

# LOOP
for i in my_cat.keys():
  print('keys -> ', i)


for v in dic_dif.values():
  print('values -> ', v)


# GET
print('get ->', my_cat.get('age', 'if not exists key age'))  # second params is optional if not exists


# SETDEFAULT
print('setdefault -> ', my_cat.setdefault('size', 'small'))


# COUNT HOW MANY CHAR AT THE STRING
string = 'It was a bright cold day in April, and the clock were striking thirteen.'
count = {}

string_upper = 'It was a bright cold day in April, and the clock were striking thirteen.'
count_upper = {}

string_lower = 'It was a bright cold day in April, and the clock were striking thirteen.'
count_lower = {}


for character in string:
  count.setdefault(character, 0)
  count[character] = count[character] + 1

for character in string_upper.upper():
  count_upper.setdefault(character, 0)
  count_upper[character] = count_upper[character] + 1


for character in string_lower.lower():
  count_lower.setdefault(character, 0)
  count_lower[character] = count_lower[character] + 1


# DEBUG
pprint.pprint(count_lower)
# print(count_lower)
# print('my cat has ' + my_cat['color'] + ' and your age is ' + str(my_cat['age']))
# print(dic_dif[2]) # num_two
# print(dic_dif[3]) # num_three

