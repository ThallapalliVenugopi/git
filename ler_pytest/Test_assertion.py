import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Test_positive_secaris:
    pass

    def open_application(self):
        driver_obj = webdriver.Chrome()
        driver_obj.get('https://www.saucedemo.com')
        driver_obj.maximize_window()
        sleep(2)
        driver_obj.find_element(By.ID, 'user-name').send_keys('standard_user')
        sleep(2)
        driver_obj.find_element(By.ID, 'password').send_keys('secret_sauce')
        sleep(2)
        driver_obj.find_element(By.ID, 'login-button').click()


