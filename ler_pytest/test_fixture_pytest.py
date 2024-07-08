import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# @pytest.fixture()
# def driver_obj():
#     print("open Chrome Driver")
#     my_driver = webdriver.Chrome()
#     yield my_driver
#     print("closing Chrome Driver ")
#     my_driver.quit()

class Test_positiv_scanarise:

    @pytest.mark.line
    @pytest.mark.positive
    def test_positive(self, driver_obj):
        driver_obj = webdriver.Chrome()
        driver_obj.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        sleep(15)
        driver_obj.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
        driver_obj.find_element(By.XPATH, "//input[@name='password']").send_keys('admin123')
        driver_obj.find_element(By.XPATH, "//button[@type='submit']").click()
