# -*- coding: utf-8 -*-

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print('the host is: ' + str(res.status_code))  # check status code
print('the host lenght is: ' + str(len(res.text)))
print('some text from host: ' + res.text[:500])