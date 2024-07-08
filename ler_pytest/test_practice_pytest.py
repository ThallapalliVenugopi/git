import pytest
#from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Test_positiv_scanarise:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver_obj):
        #driver_obj=webdriver.Chrome()
        driver_obj.get('https://www.saucedemo.com/')
        driver_obj.maximize_window()
        sleep(10)
        driver_obj.find_element(By.XPATH, "//input[@name='user-name']").send_keys('standard_user')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@name='password']").send_keys('secret_sauce')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@id='login-button']").click()
        sleep(10)

