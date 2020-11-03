from selenium import  webdriver
from time import  sleep

class seleniumMethod(object):
    def __init__(self):
        self.webdriver = webdriver.Chrome()
        self.webdriver.get("https://www.baidu.com")
        self.webdriver.maximize_window()
    def method(self):
        self.webdriver.find_element_by_id("kw").send_keys('selenium')
        sleep(2)
        self.webdriver.find_element_by_id('su').click()
        # self.webdriver.find_element_by_id("kw").send_keys('selenium')
        # sleep(2)
        # self.webdriver.find_element_by_id('su').click()
        print(self.webdriver.name)# 浏览器名称
        #print('窗口的名字')
        print(self.webdriver.current_url)
        print(self.webdriver.title)
        #print(self.webdriver.page_source)
        #当前页面源码
        #print(self.webdriver.current_window_handle)#窗口句柄
        print(self.webdriver.window_handles)#当前窗口所有句柄
        sleep(5)

        self.webdriver.close()
    def WindowOperate(self):
        sleep(3)
        self.webdriver.back()#回退
        sleep(5)
        self.webdriver.forward()#向前
        sleep(2)
        self.webdriver.refresh()#刷新
        sleep(2)
        self.webdriver.close()#关闭
    def testWindow(self):
        self.webdriver.find_element_by_link_text('新闻').click()
        print(self.webdriver.window_handles)
        window = self.webdriver.window_handles


        while 1:
            for w in window:
                self.webdriver.switch_to.window(w)
                sleep(2)
         











if __name__ =='__main__':   #执行下面的指定代码
    case = seleniumMethod()
    #case.method()
    #case.WindowOperate()
    case.testWindow()