from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_loginpage:
    __url = 'https://www.saucedemo.com'
    __username_filed = (By.ID, "user-name")
    __password_filed = (By.NAME, "password")
    __submit_button = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        print(username, password,"**********")
        wait = WebDriverWait(self._driver, 10)
        wait.until(EC.visibility_of_element_located(self.__username_filed))
        self._driver.find_element(self.__username_filed).send_keys(username)
        wait.until(EC.visibility_of_element_located(self.__password_filed))
        self._driver.find_element(self.__password_filed).send_keys(password)
        wait.until(EC.visibility_of_element_located(self.__submit_button))
        self._driver.find_element(self.__submit_button).click()


# l1 = Test_loginpage()
#
# l1.open()
# l1.execute_login("standard_user", "secret_sauce")
