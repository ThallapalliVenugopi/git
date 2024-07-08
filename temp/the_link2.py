from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get("https://the-internet.herokuapp.com")
sleep(20)
b=driver_obj.find_elements(By.TAG_NAME,"c")
for i in b:
 print("#####",i.text)

