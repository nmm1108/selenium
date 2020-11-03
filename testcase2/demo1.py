# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "capability"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermisions"] = "true"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#隐式等待
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
sleep(2)

# action = TouchAction(driver)
# action.long_press().move_to().release().perform()
# driver.swipe()#滑动
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("pdd")
# driver.implicitly_wait(10)
# el3 = driver.find_element_by_link_text('阿里巴巴')
# el3.click()
sleep(5)
driver.quit()