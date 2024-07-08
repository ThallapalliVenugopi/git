from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get("https://www.saucedemo.com/")
driver_obj.find_element(By.XPATH, "//input[@name='user-name']").send_keys("standard_user")
driver_obj.find_element(By.XPATH, "//input[@name='password']").send_keys("secret_sauce")
driver_obj.find_element(By.XPATH, "//input[@id='login-button']").click()
driver_obj.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
driver_obj.find_element(By.XPATH, "//c[@id='inventory_sidebar_link']").click()
sleep(10)