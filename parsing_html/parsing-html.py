# -*- coding: utf-8 -*-

import bs4
import requests

productURL = 'https://www.amazon.com.br/Automate-Boring-Stuff-Python-2nd-ebook/dp/B07VSXS4NK/'
"""

res = requests.get('https://www.amazon.com.br/Automate-Boring-Stuff-Python-2nd-ebook/dp/B07VSXS4NK/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elements = soup.select('#buybox > div > table > tbody > tr.kindle-price > td.a-color-price.a-size-medium.a-align-bottom span')
elements = soup.select('.a-size-medium .a-color-price')
print(elements[0].text.strip())

"""

def debug(**Kwargs):
  for keys, values in Kwargs.items():
    print('%s -> %s' %(keys, values))



def get_amazon_price(productUrl):
  res = requests.get(productURL)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  selector = '.a-size-medium .a-color-price'
  element = soup.select(selector)

  return element[0].text.strip()


price = get_amazon_price(productURL)

debug(price='The price is: ' + price)