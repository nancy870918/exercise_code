from selenium import webdriver
from time import sleep
import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://10.1.30.32:8081/')

    def test_login1(self):
        # 输入用户名
        self.driver.find_element_by_xpath("//input[@widgetcode='JGTextBox1']").clear()
        self.driver.find_element_by_xpath("//input[@widgetcode='JGTextBox1']").send_keys('liangmf')
        # 输入密码
        self.driver.find_element_by_xpath("//input[@widgetcode='JGPasswordBox1']").clear()
        self.driver.find_element_by_xpath("//input[@widgetcode='JGPasswordBox1']").send_keys(2)
        # 点击登录按钮
        self.driver.find_element_by_xpath("//*[@widgetcode='JGButton1']").click()
        sleep(2)
        ele = self.driver.find_element_by_xpath("//span[contain(test(),'欢迎您')] ").text
        print(ele)


    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
            unittest.main()




        #
        # class TestHuman_Resources(unittest.Testcase):
        #     def setup(self):
        #         print("do something before test.Prepare environment.")
        #     def tearDown(self):
        #         print("do something after test.Clean up.")
        #     def testTestCase_Application(self):
        #         print("用例1：请假申请")
        #
        #
        #
        #
        # #点击请假申请
        # driver.find_element_by_xpath("//img[starts-with(@id,'vp_hr_portal_myApply_web_JGImage1') and @class='img-responsive default pull-left']").click()
        # try:
        #     driver.find_element_by_class_name('JGFormTitle')
        #     print("请假申请已找到")
        # except :
        #     print("请假申请not found ")
        # sleep(2)
        # driver.find_element_by_class_name('close').click()
