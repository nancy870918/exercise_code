from BasePage import *
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage(Page):
    url=''

    #定位器-对相关元素进行定位
    username_loc=(By.XPATH,"//input[@widgetcode='JGTextBox1']")
    password_loc=(By.XPATH,"//input[@widgetcode='JGPasswordBox1']")
    submit_loc=(By.XPATH,"//*[@widgetcode='JGButton1']")

    def type_username(self,username):
         self.find_element(*self.username_loc).clear()
         self.find_element(*self.username_loc).send_keys(username)


    def type_password(self, password):
         self.find_element(*self.password_loc).clear()
         self.find_element(*self.password_loc).send_keys(password)


    def type_submit(self):
         self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()



