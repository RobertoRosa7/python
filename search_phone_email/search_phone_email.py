# -*- coding: utf-8 -*-

import re, pyperclip

def debug(**Kwargs):
  for key, value in Kwargs.items():
    print("%s -> %s" %(key, value))


regex_phone = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 1234, ext. 12345, x12345
(((\d\d\d)|(\(\d\d\d\)))?  # area code (optional)
(\s|-)  # first separator
\d\d\d  # first 3 digits
-  # separator
\d\d\d\d  # last 4 digits
(((ext(\.)?\s)|x)  # extension word-part (optional)
(\d{2,5}))?)  # extension number-part (optional)
''', re.VERBOSE)

regex_email = re.compile(r'''
# name@domain.com
[a-zA-Z0-9_.+]+  # name part
@  # symbol
[a-zA-Z0-0_.+]+  # domain name part
''', re.VERBOSE)

# get text off the clipboard
text = pyperclip.paste()

# extract the email/phone
extracted_phone = regex_phone.findall(text) 
extracted_email = regex_email.findall(text)

all_phone_found = []
for phone in extracted_phone:
  all_phone_found.append(phone[0])


# copy the extracted email/phone to the clipboard
results = '\n'.join(all_phone_found) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)


# debug
debug(res=results)
# debug(phone=all_phone_found)
# debug(phone=extracted_phone, email=extracted_email)  # raw debug