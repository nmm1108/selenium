from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
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

        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        sleep(2)

        # action = TouchAction(driver)
        # action.long_press().move_to().release().perform()
        # driver.swipe()#滑动
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("pdd")
        sleep(3)

    def teardown(self):
            self.driver.quit()
