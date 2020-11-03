from selenium import webdriver
from time import  sleep


url = "https://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url)
sleep(2)
driver.find_element_by_id("kw").send_keys('selenuim')
sleep(1)
driver.find_element_by_id('su').click()

sleep(5)
driver.quit()