import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import logging



@pytest.fixture()
def driver_obj():
    my_driver = webdriver.Chrome()
    yield my_driver

    my_driver.quit()


class Test_positive_login:

    @pytest.mark.mani
    @pytest.mark.thalla
    def test_positiv_log(self, driver_obj):

        driver_obj.get("https://www.saucedemo.com/")
        sleep(2)
        driver_obj.maximize_window()
        driver_obj.find_element(By.ID, 'user-name').send_keys('standard_user')
        sleep(3)
        driver_obj.find_element(By.ID, 'password').send_keys('test')
        sleep(3)
        driver_obj.find_element(By.ID, 'login-button').click()
        some_text = driver_obj.find_element(By.TAG_NAME, 'h3').text
        print(some_text)
        # logging.debug(some_text)
        logging.info("failure case message: {}".format(some_text))
        print("hellow good evening")
        assert (some_text == 'Epic sadface: Username and password do not match any user in this service')
