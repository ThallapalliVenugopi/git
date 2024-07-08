from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_obj=webdriver.Chrome()
driver_obj.get("https://the-internet.herokuapp.com")
sleep(5)
driver_obj.find_element(By.LINK_TEXT,'Broken Images').click()
images = driver_obj.find_elements(By.TAG_NAME, 'img')

for image in images:
    width = int(image.get_attribute("naturalWidth"))
    height = int(image.get_attribute("naturalHeight"))

    if width != 0 and height != 0:
        print("Image displayed")
    else:
        print("Image not displayed")