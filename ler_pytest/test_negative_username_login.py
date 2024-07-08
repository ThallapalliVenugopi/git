import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    # open chrome driver
    my_driver = webdriver.Chrome()
    yield my_driver
    # closing chrome driver
    my_driver.quit()


class Test_positiv_log:

    @pytest.mark.varun
    @pytest.mark.parametrize("username,password,expected_error_message", [
        ("secret_sauce", "secret_sauce", "Epic sadface: Username and password do not match any user in this service")])
    def test_negative_username(self, driver,username,password,expected_error_message):
        driver.get('https://www.saucedemo.com/')
        driver.find_element(By.ID, 'user-name').send_keys('username')
        sleep(2)
        driver.find_element(By.ID, 'password').send_keys('password')
        sleep(2)
        driver.find_element(By.ID, 'login-button').click()
        some_text = driver.find_element(By.TAG_NAME, "h3").text
        assert (some_text == expected_error_message)

