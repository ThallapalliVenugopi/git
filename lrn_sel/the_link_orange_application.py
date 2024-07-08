from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver_obj.maximize_window()
sleep(15)
driver_obj.find_element(By.NAME,'username').send_keys('Admin')
sleep(2)
driver_obj.find_element(By.NAME,'password').send_keys('admin123')
sleep(2)
driver_obj.find_element(By.TAG_NAME,'button').click()
sleep(2)
driver_obj.find_element(By.TAG_NAME,'span').click()
sleep(2)
driver_obj.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys('venu')
sleep(2)
driver_obj.find_element(By.XPATH,"(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
sleep(2)