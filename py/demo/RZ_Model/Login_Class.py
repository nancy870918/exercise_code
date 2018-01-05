#coding=utf-8
from selenium import webdriver
#登录登出的类
class Login():
    def user_login(self,driver,username,password):
        # 输入用户名
        driver.find_element_by_xpath("//input[@widgetcode='JGTextBox1']").clear()
        driver.find_element_by_xpath("//input[@widgetcode='JGTextBox1']").send_keys(username)
        # 输入密码
        driver.find_element_by_xpath("//input[@widgetcode='JGPasswordBox1']").clear()
        driver.find_element_by_xpath("//input[@widgetcode='JGPasswordBox1']").send_keys(password)
        # 点击登录按钮
        driver.find_element_by_xpath("//*[@widgetcode='JGButton1']").click()

    def user_logout(self,driver):
        # 退出
        driver.find_element_by_xpath("//span[text()='退出系统']").click()
        # 处理提示信息窗口
        driver.find_element_by_id('dialogConfirm').click()
        driver.quit()

#当前调用
# if __name__=='__main__':
#     #打开浏览器
#     driver = webdriver.Firefox()
#     #最大化窗口
#     driver.maximize_window()
#     # 输入地址
#     driver.get('http://10.1.30.32:8083/')
#     #自动等待加载最大时间
#     driver.implicitly_wait(3)
#
#     #调用登入登出类
#     Login().user_login(driver)
#     # Login().user_logout(driver)
#     #关闭浏览器
#     # driver.quit()

