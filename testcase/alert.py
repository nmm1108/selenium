from selenium import webdriver
from time import sleep
import os

class Alerts(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        path=os.path.dirname(os.path.abspath(__file__))
        path_file='file:///'+path+'/alert.html'
        self.driver.get(path_file)

    def alerts(self):
        self.driver.find_element_by_id('alert').click()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.quit()

    def confirm(self):
        self.driver.find_element_by_id('confirm').click()
        sleep(2)
        #self.driver.switch_to.alert.dismiss()
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.close()

    def prompt(self):
        self.driver.find_element_by_id('prompt').click()
        sleep(2)
        self.driver.switch_to.alert.send_keys('20')
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.quit()




if __name__ =='__main__':
    case=Alerts()
    #case.alerts()
    #case.confirm()
    case.prompt()

