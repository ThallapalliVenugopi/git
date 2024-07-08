from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get("https://the-internet.herokuapp.com")
sleep(5)
driver_obj.find_element(By.LINK_TEXT,'Checkboxes').click()
sleep(2)
driver_obj.find_element(By.TAG_NAME,'input').click()
sleep(2)
driver_obj.find_element(By.TAG_NAME,'input').click()
sleep(2)
# driver_obj.find_element(By.TAG_NAME,'')
# sleep(2)