# -*- coding: utf-8 -*-

# LOOPS
someList = [1, 2, 3, 4]
otherList = list(range(0, 100, 2))
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

# BASICS
# for a in range(4):
#   print(a)

# for b in ['a','b','c','d','e']:
#   print(a)

# for c in list(range(4)):
#   print(c)

# for d in list('Hello world'):
#   print(d)


# for i in range(len(otherList)):
#   print(i)
for i in range(len(supplies)):
  print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
