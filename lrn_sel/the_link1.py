import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.set_page_load_timeout(100)
driver_obj.get("https://the-internet.herokuapp.com")
time.sleep(20)
driver_obj.maximize_window()
driver_obj.find_element(By.LINK_TEXT,"Add/Remove Elements").click()
sleep(5)
a=driver_obj.find_element(By.XPATH, "//button[text()='Add Element']").click()

sleep(5)
driver_obj.find_element(By.XPATH, "//button[text()='Add Element']").click()
sleep(5)
driver_obj.find_element(By.XPATH, "//button[text()='Add Element']").click()
a=driver_obj.find_elements(By.CSS_SELECTOR,'.added-manually')
print("###########", len(a))
a=driver_obj.find_elements(By.CLASS_NAME,'added-manually')
print("$$$$$$$$$$$$$", len(a))
sleep(5)

driver_obj.find_element(By.CLASS_NAME,'added-manually').click()
sleep(5)
driver_obj.find_element(By.CLASS_NAME,'added-manually').click()
sleep(5)
driver_obj.find_element(By.CLASS_NAME,'added-manually').click()
sleep(5)
a=driver_obj.find_elements(By.CSS_SELECTOR,'.added-manually')
print(len(a))
