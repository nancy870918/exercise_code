from selenium import webdriver
from time import sleep
import unittest
from redmine_page import LoginPage,Login,LeavePage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://10.1.27.52:9011')

    @unittest.skip("测试跳过")
    def test_case1_login(self):
        loginpage = LoginPage(self.driver) #实例化登录页面对象
        loginpage.enter_username()
        loginpage.enter_passward()
        loginpage.click_login()
        ele = loginpage.get_login_name()
        self.assertIn('欢迎您',ele)

    # @unittest.skip("test pass")
    def test_case2_leave_application(self):
        Login(self.driver).user_login()
        leaveappliction = LeavePage(self.driver)
        leaveappliction.enter_leave_butten()
        sleep(2)
        leaveappliction.enter_leave_type()
        sleep(2)
        leaveappliction.enter_leave_reason()
        leaveappliction.enter_date_time()
        ele = leaveappliction.sucess_content
        self.assertIn('提交成功', ele)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
            unittest.main()




