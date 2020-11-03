from selenium import webdriver
from time import sleep, strftime, localtime, time
import os

class TestScreenShot(object):
    def __init__(self):
        self.driver =webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def screenShot(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        #self.driver.save_screenshot('baidu.png')
        # st = strftime("%Y-%m-%d-%H-%M-%S",localtime(time())) #本地化时间
        # file_name = st + '.png'
        # self.driver.save_screenshot(file_name)

        st = strftime("%Y-%m-%d-%H-%M-%S",localtime(time())) #本地化时间
        file_name = st + '.png'

        path = os.path.abspath('screenshot')
        file_path = path + '/' + file_name
        self.driver.save_screenshot(file_path)

if __name__ == '__main__':
    case = TestScreenShot()
    case.screenShot()
