from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_obj = webdriver.Chrome(service=Service("C:\\browserdrivers\\chromedriver.exe")) #driver object
driver_obj.get("https://www.vagdevitechnologies.com") #loading the page
print(driver_obj.title) #to return the title
print(driver_obj.current_url) #to return the url of the current_page
driver_obj.find_element_by_xpath("//*[@id='post-2']/div/div/div/section[1]/div[2]/div/div/section/div/div/div/div[3]/div/div/c/span/span[2]").click()

sleep(10)
driver_obj.close()