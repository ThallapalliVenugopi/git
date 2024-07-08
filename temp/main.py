from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://facebook.com')
driver.maximize_window()

sleep(2)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys('9705960947')
driver.find_element(By.XPATH, "//input[@name='pass']").send_keys('9000454732')
driver.find_element(By.XPATH, "//button[@name='login']").click()
sleep(10)