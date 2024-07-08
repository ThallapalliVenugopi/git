from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from src.practice_page_elements import PracticeElements

p_elements = PracticeElements();
driver_obj=webdriver.Chrome()
driver_obj.get(p_elements.url)
driver_obj.maximize_window()
driver_obj.find_element(By.XPATH, p_elements.bmwradio).click()
# sleep(5)
#driver_obj.find_element(By.XPATH, "//input[@value='bmw']").click()
#sleep(5)
driver_obj.find_element(By.XPATH, p_elements.cars).click()
sleep(5)
# driver_obj.find_element(By.XPATH, "//input[@type='radio']").click()
# sleep(5)