from selenium import webdriver
from time import sleep
import os

class CheckHtml(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        filepath = 'file:///' + path + '/form2.html'
        self.driver.get(filepath)
        #self.driver.get('https://www.baidu.com')

    def check(self):
        swimming = self.driver.find_element_by_name('swimming')
        if not swimming.is_selected():
            swimming.click()
        read = self.driver.find_element_by_name('reading')
        if not read.is_selected():
            read.click()
        sleep(2)

        swimming.click()
        read.click()
        sleep(3)
        self.driver.quit()

    def radio(self):
        gender = self.driver.find_elements_by_name('gender')
        gender[0].click()
        sleep(2)
        gender[1].click()
        sleep(3)
        # gender.clear()
        # sleep(3)
        self.driver.close()


if __name__ == '__main__':
    case = CheckHtml()
    #case.check()
    case.radio()


