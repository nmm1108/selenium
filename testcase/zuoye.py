from selenium import webdriver
from time import sleep
import os


# class BiaoDan(object):
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         path = os.path.dirname(os.path.abspath(__file__))
#         file_path = 'file:///' + path + '/form.html'
#         self.driver.get(file_path)
#
#     def open_html(self):
#         usersname = self.driver.find_element_by_id('usersname')
#         usersname.send_keys('admin')
#         pwd = self.driver.find_element_by_id('pwd')
#         pwd.send_keys('pwd')
#         sleep(2)
#         self.driver.find_element_by_id('submit').click()
#
#         self.driver.switch_to.alert.accept()
#
#         sleep(2)
#
#         print(usersname.get_attribute('value'))
#         print(pwd.get_attribute('value'))
#         print('清理前的值：' + usersname.get_attribute('value'))
#         print('清理前的值：' + pwd.get_attribute('value'))
#         usersname.clear()
#         pwd.clear()
#         print('清理后的值：' + usersname.get_attribute('value'))
#         print('清理后的值：' + pwd.get_attribute('value'))
#         sleep(2)
#         self.driver.close()


class CheckHtml(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form2.html'
        self.driver.get(file_path)

    def checks(self):
        swimming = self.driver.find_element_by_name('swimming')
        if not swimming.is_selected():
            swimming.click()
        read = self.driver.find_element_by_name('reading')
        if not read.is_selected():
            read.click()
        sleep(2)

        swimming.click()
        read.click()
        sleep(2)
        self.driver.quit()

    def radios(self):
        gender = self.driver.find_elements_by_name('gender')
        for i in gender:
            i.click()
            sleep(3)
        self.driver.close()



if __name__ == '__main__':
    # case = BiaoDan()
    # case.open_html()
    case = CheckHtml()
    #case.checks()
    case.radios()