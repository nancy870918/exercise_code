# -*- coding: utf-8 -*-
from Login_Class import *
driver=webdriver.Firefox()
# 最大化窗口
driver.maximize_window()
# 输入地址
driver.get('http://10.1.30.32:8081/')
# 自动等待加载最大时间
driver.implicitly_wait(4)
Login().user_login(driver,'liangmf',2)


