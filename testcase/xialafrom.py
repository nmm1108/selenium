from selenium import  webdriver
from time import sleep
import os

from selenium.webdriver.support.select import Select


class XiaLaForm(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path +'/xialaform.html'
        self.driver.get(file_path)

    def selects(self):
        se = self.driver.find_element_by_name('provide')
        select = Select(se)
        # select.select_by_index(0)
        #
        # sleep(2)
        # select.select_by_value("tj")
        # sleep(2)
        # select.select_by_visible_text("上海")
        # sleep(2)

        for i in range(3):
            select.select_by_index(i)
            sleep(2)
        select.deselect_all()
        sleep(2)

        for option in select.options:
            print(option.text)
            sleep(2)


        self.driver.quit()




if __name__ == '__main__':
    case = XiaLaForm()
    case.selects()