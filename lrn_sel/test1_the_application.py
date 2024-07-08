from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver_obj.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver_obj.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123" )
driver_obj.find_element(By.CLASS_NAME,'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button').click()
sleep(10)