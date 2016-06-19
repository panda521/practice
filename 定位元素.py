# -*- coding: utf-8 -*-
from selenium import webdriver
from time import time

browser = webdriver.Ie()
browser.get("http://www.baidu.com")

#通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")

#通过name方式定位
browser.find_element_by_name("kd").send_keys("selenium")

#通过tag name方式定位
browser.find_element_by_id("input").send_keys("selenium")

#通过class方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")

#通过css方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")

#通过xpath方式定位
browser.find_element_by_css_selector("//input[@id='kw']").send_keys("selenium")

browser.find_element_by_id("su").click()

time.sleep(3)

browser.quit()
