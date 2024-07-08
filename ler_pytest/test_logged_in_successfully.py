from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class loggedInsuccessfullypage:
    _url = "https://www.saucedemo.com"
    __username_filed = (By.ID, "user-name")
    __password_filed = (By.NAME, "password")
    __submit_button = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        self.driver = driver
    @property
    def current_url(self) -> str:
        return self._driver.actual_url
    @property
    def expected_url(self) -> str:
        return self._url


    def username(self) ->str:
        return self._driver.find_element(self.__username_filed)

    def pwd(self) -> str:
        return self._driver.find_element(self. __password_filed)





