# -*- coding: utf-8 -*-
import unittest


class ExampleCase1(unittest.TestCase):
    u'''此class包含两个用例：add - ok， minus - FAIL'''
    def setUp(self):
        self.a = 4
        self.b = 3

    def test_add(self):
        u'''用例1，add，此用例成功通过'''
        self.assertEqual(self.a + self.b, 7)

    def test_minus(self):
        u'''用例2，minus，此用例执行失败，4-3！=2'''
        print(u'中文xxxxxxxxxxxxxxxxxxxx')
        self.assertEqual(self.a - self.b, 2)


class ExampleCase2(unittest.TestCase):
    u'''此class包含一个用例：plus - ERROR'''
    def setUp(self):
        self.a, self.b = 4, 3

    def test_plus(self):
        u'''用例3，plus，此用例执行出错，因为c未定义'''
        self.assertEqual(self.a * self.b, c)


class ExampleCase3(unittest.TestCase):
    u'''此class包含一个用例：divide - ok'''
    def setUp(self):
        self.a, self.b = 4, 2

    def test_devide(self):
        u'''用例4，divide，此用例执行成功'''
        self.assertEqual(self.a / self.b, 2)


if __name__ == '__main__':
    from HTMLTestRunner import HTMLTestRunner
    report_title = u'Example用例执行报告'
    desc = u'用于展示修改样式后的HTMLTestRunner'
    report_file = 'D:\\ExampleReport.html'

    testsuite = unittest.TestSuite()
    testsuite.addTest(ExampleCase1("test_add"))
    testsuite.addTest(ExampleCase1("test_minus"))
    testsuite.addTest(ExampleCase2("test_plus"))
    testsuite.addTest(ExampleCase3("test_devide"))

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)