from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select



class webAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()

    'this is a wait time'

    def waittime(self):
        sleep(10)

    'this is a radio button'

    def click_radiobutton(self):
        self.driver.get('https://www.letskodeit.com/practice')
        'this maximize_window'
        self.driver.maximize_window()
        'this is a using css selector using ID'
        self.driver.find_element(By.CSS_SELECTOR, 'input#bmwradio').click()
        sleep(5)
        'this is a using css selector using CLASS'
        self.driver.find_element(By.CSS_SELECTOR, 'input#benzradio').click()
        sleep(5)
        'this is a using css selector using XPATH'
        self.driver.find_element(By.XPATH, '//input[@value="honda"]').click()
        sleep(5)

    def check_button(self):
        self.driver.find_element(By.XPATH, '//input[@name="cars"][@id="bmwcheck"]').click()
        sleep(5)
        self.driver.find_element(By.XPATH, '//input[@type="checkbox"][@id="benzcheck"]').click()
        sleep(5)
        self.driver.find_element(By.XPATH, '//input[@value="honda"][@id="hondacheck"]').click()
        sleep(5)

    #def Test_switch_window(self):
        #self.driver.find_element(By.XPATH, '//button[@id="openwindow"]').click()
        #sleep(5)
        #handles = self.driver.window_handles
       # for handle in handles:
            #self.driver.switch_to.window(handle)
            #print(self.driver.tittle)
        #self.driver.back()

    def drowp_down(self):
        x = self.driver.find_element(By.XPATH,'//select[@id="carselect"]')
        drop = Select(x)
        sleep(2)
        drop.select_by_value('bmw')
        sleep(5)
        drop.select_by_value('benz')
        sleep(5)
        drop.select_by_value('honda')
        sleep(5)


s1 = webAutomation()
s1.waittime()
s1.click_radiobutton()
s1.check_button()
#s1.Test_switch_window()
s1.drowp_down()
