from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def jsAlert(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.close()

    def Title(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)
        sleep(2)
        self.driver.close()

    def jsStyle(self):
        js = 'var q = document.getElementById("kw"); q.style.border = "2px solid red" '
        sleep(3)
        self.driver.execute_script(js)
        # sleep(5)
        # self.driver.close()

    def scroll(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(5)
        self.driver.close()



if __name__ == '__main__':
    case = TestCase()
    #case.jsAlert()
    #case.Title()
    # case.jsStyle()
    case.scroll()