# -*- coding: utf-8 -*-
from selenium import webdriver
from Login_Class import *
driver=webdriver.Firefox()
# 最大化窗口
driver.maximize_window()
# 输入地址
driver.get('http://hr.toone.com.cn/module-operation!executeOperation?operation=Form&componentCode=vp_hr_recruitment_web&windowCode=login')
# 自动等待加载最大时间
driver.implicitly_wait(4)

#调用登录方法
Login().user_login(driver,'wangls','wangls')

