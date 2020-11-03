from selenium import webdriver
from time import  sleep
from selenium.webdriver.remote.webelement import WebElement

#http://sahitest.com/demo/

class webElements(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        e = self.driver.find_element_by_id('t1')
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)
        sleep(3)
        self.driver.close()

    def test_webelement_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world')
        print(e.get_attribute('type'))
        print(e.get_attribute('name'))#不懂的地方，获得的是什么属性值
        print(e.get_attribute('value'))

        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))
        e.clear()
        print('清除后')
        print(e.get_attribute('value'))
        print('清除后')

        sleep(2)
        self.driver.close()










if __name__ == '__main__':
    case = webElements()
    #case.test_webelement_prop()
    case.test_webelement_method()
