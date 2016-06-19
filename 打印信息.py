# -*- coding: utf-8 -*-
from selenium import webdriver

browser = webdriver.Ie()
browser.get("http://www.baidu.com")
#打印title
print(browser.title)
#打印URL
print(browser.title)

browser.quit()
