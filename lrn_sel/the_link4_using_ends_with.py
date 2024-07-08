from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get("https://the-internet.herokuapp.com")
sleep(5)
driver_obj.find_element(By.LINK_TEXT,'Challenging DOM').click()
sleep(5)

for i in range(5):
    for j in range(1, 4):
        a=driver_obj.find_element(By.XPATH, f"(//a[contains(@id, '7e05d70f6739')])[{j}]").click()
        sleep(2)


