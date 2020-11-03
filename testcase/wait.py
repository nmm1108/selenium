from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #expected_conditions期待条件出现


class Wait(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def sleeps(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        sleep(2)# 线程阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.quit()

    def implicitly(self):
        self.driver.implicitly_wait(10)#隐式等待
        self.driver.find_element_by_id('kw').send_keys('selenium')
        #sleep(2)# 线程阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        #sleep(2)
        self.driver.quit()

    def waits(self):
        wait = WebDriverWait(self.driver,2)#显示等待，2秒；引入WebDriverWait方法，按住Ctrl点击
        wait.until(EC.title_is('百度一下，你就知道'))#等待标题为百度一下，你就知道出来后，在执行下面的代码
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # sleep(2)# 线程阻塞 blocking wait
        self.driver.find_element_by_id('su').click()
        # sleep(2)
        self.driver.quit()





if __name__ == '__main__':
    case = Wait()
    #case.sleeps()
    #case.implicitly()
    case.waits()


