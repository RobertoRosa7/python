# -*- coding: utf-8 -*-

"""
Controlling the Browser with Seleninum Module
"""
from selenium import webdriver

browser = webdriver.Firefox() # choose the browser
browser.get('https://automatetheboringstuff.com')  # open site
elem = browser.find_element_by_css_selector('div.main div ul li a')  # find element
# elem.text  # print raw text
# elem.click()  # event click
# elem.submit()  # event submit
# elem.send_keys('input text here')  # event input text on form

# browser.back()  # back to history browser
# browser.forward()  # to go
# browser.refresh()  # update page
# broser.quit()  # close the browser