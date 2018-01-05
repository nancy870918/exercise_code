#coding:utf-8

from setting.OpenBrowser import openBrowser
class   ElementsIde(object):
    def __init__(self):
        self.driver = openBrowser().driver

    def elementID(self, value):
        _ByID = self.driver.find_element_by_id(value)
        return _ByID

    def elementName(self, value):
        _ByName = self.driver.find_element_by_name(value)
        return _ByName

    def elementClass(self, value):
        _ByClass = self.driver.find_element_by_class(value)
        return _ByClass

    def elementXpath(self, value):
        _ByXapth = self.driver.find_element_by_xpath(value)
        return _ByXapth

    def elementLinkText(self, value):
        _ByLinkText = self.driver.find_element_by_link_text(value)
        return _ByLinkText

    def elementClassName(self, value):
        _ByClassName = self.driver.find_element_by_class_name(value)
        return _ByClassName