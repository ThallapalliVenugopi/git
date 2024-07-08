from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver_obj=webdriver.Chrome()
driver_obj.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
sleep(5)
x=driver_obj.find_element(By.XPATH,"//input[@name='username']")
x.send_keys('Admin')
x=driver_obj.find_element(By.XPATH,"//input[@name='password']")
x.send_keys('admin123')
x=driver_obj.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(10)
driver_obj.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").click()
sleep(30)
driver_obj.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys('venu')
sleep(5)
# drop=driver_obj.find_element(By.XPATH,"//input[@class='oxd-select-text oxd-select-text--active']").click()
# sleep(5)
driver_obj.find_element(By.XPATH,"((//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
sleep(20)