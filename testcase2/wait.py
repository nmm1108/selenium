import datetime

from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "capability"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermisions"] = "true"
        caps["ensureWebviewsHavePages"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #隐式等待
        self.driver.implicitly_wait(10)
    def test_demo(self):
        def loaded(driver):
            print(datetime.datetime.now())
            if len(self.driver.find_element_by_id("image_cancel"))>=1:
                self.driver.find_element_by_id("image_cancel").click()
                return True
            else:
                return False
        try:
            WebDriverWait(self.driver,20).until(loaded)
        except:
            print("no update")


        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("pdd")

    def teardown(self):
            self.driver.quit()
