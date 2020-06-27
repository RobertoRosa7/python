# -*- coding: utf-8 -*-
import re

"""
Expression Regular Basic
"""
message = 'Hello my phone number is: 55-11-94161-6008, anyway, you can call me in 55-11-3602-0022'
phone_found = []
mobile_regex = re.compile(r'\d\d-\d\d-\d\d\d\d\d-\d\d\d\d')
landline_regex = re.compile(r'\d\d-\d\d-\d\d\d\d-\d\d\d\d')

match_mobile = mobile_regex.search(message)
match_landline = landline_regex.search(message)

print('mobile found', match_mobile.group())
print('landline found', match_landline.group())
print('find all', mobile_regex.findall(message))
print('find all', landline_regex.findall(message))


def notification(msg):
  print(msg)


def is_phone_number(number):
  if len(number) != 12:
    notification('not phone size')  # not phone size
    return False
  for i in range(0, 3):
    if not number[i].isdecimal():
      notification('not code area')  # not code area
      return False
  if number[3] != '-':
    notification('missing dash')  # missing dash
    return False
  for i in range(4, 7):
    if not number[i].isdecimal():
      notification('not first 3 digits')  # not first 3 digits
      return False
  if number[7] != '-':
    notification('missing second dash')  # missing second dash
    return False
  for i in range(8, 12):
    if not number[i].isdecimal():
      notification('missing last 4 digits')  # missing last 4 digits
      return False
  return True


def is_phone_number_enhance(number):
  try:
    if '-' in number:
      split_phone = number.split('-')
      if len(split_phone[0]) != 2:
        return {'status': False, 'message': 'code country 2 digits'}
      elif len(split_phone[1]) != 2:
        return {'status': False, 'message': 'code area 2 digits'}
      elif len(split_phone[2]) == 5 and int(split_phone[2][0]) == 9:
        return {'status': True, 'message': 'is mobile phone'}
      elif len(split_phone[2]) == 4 and int(split_phone[2][0]) != 9:
        return {'status': True, 'message': 'is landline'}
      else:
        return {'status': False, 'message': 'not phone valid'}
    else:
      return {'status': False, 'message': 'not a phone number'}
  except ValueError:
    return {'status': False, 'message': 'not a number phone'}


def search_phone(text):
  flag_number = False
  for i in range(len(text)):
    if is_phone_number_enhance(text[i:i+16])['status']:
      flag_number = True
      phone_found.append(text[i:i+16])

  if not flag_number:
    print('could not find any phone numbers')
