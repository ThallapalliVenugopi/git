import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Test_positive_scanarise:

    @pytest.mark.line
    @pytest.mark.log
    def test_positive_login(self,driver_obj):
        driver_obj = webdriver.Chrome()
        driver_obj.get('https://www.saucedemo.com/')
        driver_obj.maximize_window()
        sleep(5)
        driver_obj.find_element(By.ID,'').send_keys('standard_user')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@name='password']").send_keys('secret_sauce')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@id='login-button']").click()
        sleep(10)

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self,driver_obj):
        driver_obj=webdriver.Chrome()
        driver_obj.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        sleep(10)
        driver_obj.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@name='password']").send_keys('admin123')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(10)

