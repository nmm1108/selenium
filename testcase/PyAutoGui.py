import pyautogui
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains


def test1():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')
    ele = driver.find_element_by_id('agree')
    # ele.pyautogui
    action = ActionChains(driver)
    action.move_to_element(ele).click().perform()
    sleep(5)
