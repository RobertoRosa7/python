# -*- coding: utf-8 -*-
import re

"""
Expression Regular Basic
re.DOTALL               - Include break line
re.I or re.IGNORECASE   - Ignore case sensitive
re.VERBOSE              - use multiple line options
"""

message = 'Hello my phone number is: 55-11-94161-6008, anyway, you can call me in 55-11-3602-0022'
phone_found = []
mobile_regex = re.compile(r'\d\d-\d\d-\d\d\d\d\d-\d\d\d\d')
landline_regex = re.compile(r'\d\d-\d\d-\d\d\d\d-\d\d\d\d')

match_mobile = mobile_regex.search(message)
match_landline = landline_regex.search(message)


def notification(**Kwargs):
  for key, value in Kwargs.items():
    print("%s -> %s" %(key, value))


notification(
  mobileFound=match_mobile.group(), 
  landline=match_landline.group(),
  mobileFindAll=mobile_regex.findall(message),
  landlineFindAll=landline_regex.findall(message))


def match_strings(string):
  try:
    res = re.compile(r'Bat(wo)?man').search(string).group()  # wo is opcional
    any_string_one = re.compile(r'(ha){3}').search(string).group()
    bats_one = re.compile(r'Bat(man|mobile|copter|bat)').search(string).group()  # or

    notification(match=res, anyString=any_string_one, batFound=bats_one)
  except AttributeError:
    notification(message='Nenhum resultado encontrado')


def search_number_phone(number):
  phone_number = re.compile(r'(\d\d)-(\d\d\d\d\d-\d\d\d\d)')
  phone_number_space = re.compile(r'\(\d\d\) (\d\d\d\d\d-\d\d\d\d)')  # use \(and\) to match literal parenteses
  ddd_opcional = re.compile(r'(\d\d)? (\d\d\d\d\d-\d\d\d\d)')  # DDD is opcional

  try:
    mo = phone_number.search(number).group()  # print all group
    mo1 = phone_number.search(number).group(1)  # print first group
    mo2 = phone_number.search(number).group(2)  # print second group
    mos = phone_number_space.search(number).group()
    ddd = ddd_opcional.search(number).group()

    notification(groupOne=mo, groupTwo=mo1, groupThree=mo2, grougSpace=mos, ddd=ddd)
  except AttributeError:
    notification(message='Não foi encontrado nenhum número valido de celular\nEx: 11-91234-5678\nAttributeError')
  except TypeError:
    notification(message='Não foi encontrado nenhum número valido de celular\nEx: 11-91234-5678\nTypeError')


def is_phone_number(number):
  if len(number) != 12:
    notification(sizePhone='not phone size')  # not phone size
    return False
  for i in range(0, 3):
    if not number[i].isdecimal():
      notification(codeArea='not code area')  # not code area
      return False
  if number[3] != '-':
    notification(missDash='missing dash')  # missing dash
    return False
  for i in range(4, 7):
    if not number[i].isdecimal():
      notification(firstThreeDigits='not first 3 digits')  # not first 3 digits
      return False
  if number[7] != '-':
    notification(secondDash='missing second dash')  # missing second dash
    return False
  for i in range(8, 12):
    if not number[i].isdecimal():
      notification(lastDigits='missing last 4 digits')  # missing last 4 digits
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


def find_all_expression():
  find_all_any = re.compile(r'.at').findall('the cat in the hat sat on the flat mat')  # any character
  find = re.compile(r'^\d+$').search('123424023408').group()  # everything that begins and ends with numbers
  the_first_and_the_last_name = re.compile(r'First name: (.*) Last name: (.*)').findall('First name: Roberto Last name: Rosa')
  search_anything = re.compile(r'<(.*?)>').findall('<Hello> is real>')
  search_with_new_line = re.compile(r'.*', re.DOTALL).search('is\nother\nnew line').group()
  search_and_ignore_case = re.compile(r'[aeiou]', re.IGNORECASE).findall('Al, why you does your programming book talk')

  notification(
    a=find, 
    b=find_all_any, 
    c=the_first_and_the_last_name, 
    d=search_anything,
    e=search_with_new_line,
    i=search_and_ignore_case
  )


def replace_string():
  text = 'Agent Roberto gave the secret documents to Agent Alice, +55 11 94161-6008'

  search_name = re.compile(r'Agent \w+').findall(text)
  replace_name = re.compile(r'Agent (\w)\w*').sub(r'Agent \1******', text)
  use_verbose = re.compile(r'''
  (\d\d) |      # area code with parens
  (\(\d\d)\)    # -or- area code with parens and no dash
  -
  \d\d\d\d\d   # first term
  -
  \d\d\d       # last term
  \sx\d{2,4}   # extension, like x1234
  ''', re.VERBOSE | re.IGNORECASE | re.DOTALL).findall(text)

  notification(a=search_name, b=replace_name, c=use_verbose)


replace_string()