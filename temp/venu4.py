from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get("https://www.saucedemo.com/")
driver_obj.find_element(By.XPATH, "//input[@name='user-name']").send_keys("standard_user")
driver_obj.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver_obj.find_element(By.XPATH, "//input[@id='login-button']").click()
sleep(10)
width=500
hight=(400)
driver_obj.set_window_size(width,hight)
sleep(10)