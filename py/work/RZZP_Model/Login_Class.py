# -*- coding: utf-8 -*-
import time
class Login():
    def user_login(self,driver,username,password):
        '''登录招聘系统'''
        driver.find_element_by_xpath("//input[starts-with(@id,'vp_hr_recruitment_web_login_JGTextBox1') and @class='form-control input-md']").send_keys(username)
        driver.find_element_by_xpath("//input[starts-with(@id,'vp_hr_recruitment_web_login_JGPasswordBox1') and @type='password']").send_keys(password)
        time.sleep(8)
        driver.find_element_by_xpath("//button[starts-with(@id,'vp_hr_recruitment_web_login_JGButton1') ]").click()
        time.sleep(2)
        title = driver.find_element_by_xpath("//p[starts-with(@id,'vp_hr_recruitment_web_index_JGLabel4') ]").text  # 获取登录的标题
        '''验证是否登录成功'''
        try:
            assert title == u'欢迎您，'
            return '登录成功'

        except AssertionError as e:
            return '登录失败'

    def user_logout(self,driver):
        # 退出
        driver.find_element_by_xpath("//span[@class='LabelText' and text()='退出']").click()
        driver.quit()



