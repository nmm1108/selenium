from selenium import webdriver
from time import  sleep
import os

class BiaoDan(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))

        file_path = 'file:///' + path + '/form.html'
        # os.path.abspath(__file__)获取当前脚本的完整路径
        # //语法：os.path.dirname(path) 功能：去掉文件名，返回目录
        # print(os.path.dirname('W:\Python_File\juan之购物车.py'))
        # 结果
        # W:\Python_File
        # print(os.path.dirname('W:\Python_File'))
        # 结果
        # W:\

        self.driver.get(file_path)

    def open_html(self):
        usersname = self.driver.find_element_by_id('usersname')
        usersname.send_keys('admin')
        sleep(2)
        pwd = self.driver.find_element_by_id('pwd')
        pwd.send_keys('pwd')

        print(usersname.get_attribute('value'))
        print(pwd.get_attribute('value'))

        self.driver.find_element_by_id('submit').click()
        self.driver.switch_to.alert.accept()
        sleep(2)

        usersname.clear()
        print(usersname.get_attribute('value'))
        print('清理后')
        sleep(3)
        self.driver.close()


if __name__ == '__main__':
        case= BiaoDan()
        case.open_html()