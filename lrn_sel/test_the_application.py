from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get("https://www.saucedemo.com")
driver_obj.maximize_window()
driver_obj.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver_obj.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
driver_obj.find_element(By.XPATH,"//input[@id='login-button']").click()
sleep(10)
driver_obj.find_element(By.ID,'react-burger-menu-btn').click()
sleep(5)
driver_obj.find_element(By.ID,'inventory_sidebar_link').click()
sleep(15)