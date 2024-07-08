import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture()
def driver_obj():
    my_driver = webdriver.Chrome()
    yield my_driver
    my_driver.quit()


class Test_positive_scanarise:

    @pytest.mark.gopi
    @pytest.mark.line
    @pytest.mark.parametrize("user_name, password, expted_error_message",
                             [('inncorect', 'secret_sause', 'expted_error_message'),
                              ('standard_user', 'incorect password', 'expted_error_message'),
                              ('standard_user', 'secret_sause','expted_error_message')])
    def test_negative_login(self, driver_obj, user_name, password, expted_error_message):
        # driver_obj = webdriver.Chrome()
        driver_obj.get('https://www.saucedemo.com/')
        driver_obj.maximize_window()
        sleep(5)
        driver_obj.find_element(By.ID, "user-name").send_keys('inncorect')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@name='password']").send_keys('secret_sause')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@id='login-button']").click()
        sleep(10)
        error_message_locator = driver_obj.find_element(By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']")
        assert error_message_locator.is_displayed(), "error message not displayed,but in should be"

        error_message = error_message_locator.text
        assert error_message == 'Epic sadface: Username and password do not match any user in this service'

    def test_negative_username(self, driver_obj):
        #driver_obj = webdriver.Chrome()
        driver_obj.get('https://www.saucedemo.com/')
        driver_obj.maximize_window()
        sleep(5)
        driver_obj.find_element(By.ID, "user-name").send_keys('standard_user')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@name='password']").send_keys('incorect password')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@id='login-button']").click()
        sleep(10)
        error_message_locator = driver_obj.find_element(By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']")
        assert error_message_locator.is_displayed(), "error message not displayed,but in should be"

        error_message = error_message_locator.text
        assert error_message == 'Epic sadface: Username and password do not match any user in this service'

    def test_positive_login(self, driver_obj):
        #driver_obj = webdriver.Chrome()
        driver_obj.get('https://www.saucedemo.com/')
        driver_obj.maximize_window()
        sleep(5)
        driver_obj.find_element(By.ID, "user-name").send_keys('standard_user')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@name='password']").send_keys('secret_sauce')
        sleep(3)
        driver_obj.find_element(By.XPATH, "//input[@id='login-button']").click()
        sleep(10)
        error_message_locator = driver_obj.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "error message not displayed,but in should be"

        error_message = error_message_locator.text
        assert error_message == 'your user password is invalid', 'error message not expted'
