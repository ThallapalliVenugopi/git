from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get('https://www.saucedemo.com/')
print(driver_obj.title)
print(driver_obj.current_url)
print(driver_obj.page_source)
sleep(20)
