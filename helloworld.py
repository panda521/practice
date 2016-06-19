# -*- coding: utf-8 -*-
from selenium import webdriver

browser = webdriver.Ie()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

browser.implicitly_wait(30)  #智能等待30秒

browser.quit()
