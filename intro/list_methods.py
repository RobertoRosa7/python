# -*- coding: utf-8 -*-

# LIST METHODS
theList = ['hello', 'hi', 'how are you?', 1, 5, -3, 'H', 'A', 'a']

# METHOD INDEX()
# print(theList.index('hi')) # 1
# print(theList.index('how are you?')) # 2
# print(theList.index('how are you')) # ValueError
# try:
#   print(theList.index('how are you'))
# except ValueError:
#   print('Not found')

# METHOD INSERT() APPEND()
theList.insert(0, 'insert method')  # add item on specific area
only_strings = []
only_numbers = []

# METHOD REMOVE()
theList.remove('hi')


# METHOD SORT()
def split_and_order():
  for i in range(len(theList)):
    if type(theList[i]) == str:
      only_strings.append(theList[i])
    elif type(theList[i]) == int:
      only_numbers.append(theList[i])
  only_numbers.sort()
  only_strings.sort()
  print(only_numbers + only_strings)


def eggs(some_parameter):
  some_parameter.append('Hello')


num = [1, 2, 3]
eggs(num)
print(num)

# theList.sort() # sort basic
# theList.sort(reverse=True) # reverse order
only_strings.sort(key=str.lower)  # convert to lowercase
# theList.sort(key=str.upper)  # convert to uppercase

# DEBUG
# print(only_strings)
