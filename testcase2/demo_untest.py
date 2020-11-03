from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from  unittest import TestCase

from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestDemo(TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "capability"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermisions"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps["unicodeKeyboard"] = True #可以输入中文设置

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #隐式等待
        self.driver.implicitly_wait(10)
    def test_demo(self):

        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("pdd")

    def test_capdbilities(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("拼多多")
        sleep(3)

    def test_gsm_call(self):
        self.driver.send_sms("15927695572","hello,from seveniruby")
        self.driver.make_gsm_call("15927695572",GsmCallActions.CALL)

    def tearDown(self):
            self.driver.quit()

