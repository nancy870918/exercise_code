#coding:utf-8
# import yaml
# y = yaml.load(open('test1.yaml','r',encoding="utf-8"))
# print(y)
# for i in y:
#     print(i)
# # print(type(y))
# # print(y.get('name'))

import  yaml
from selenium import webdriver
import time
y = yaml.load(open('url.yaml','r'))
url = y.get('URL')

driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)
driver.quit()