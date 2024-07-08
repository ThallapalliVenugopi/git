from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.letskodeit.com/practice')
x=driver.find_element(By.XPATH,"//select[@id='carselect']")
drop=Select(x)
#drop.select_by_index('0')
#drop.select_by_visible_text('BMW')
drop.select_by_value('bmw')
sleep(5)
#drop.select_by_index('1')
#drop.select_by_visible_text('Benz')
drop.select_by_value('benz')
sleep(5)
#drop.select_by_index('2')
#drop.select_by_visible_text('Honda')
drop.select_by_value('honda')
sleep(10)