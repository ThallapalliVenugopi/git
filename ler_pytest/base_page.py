from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

[1, 2, [3, 4, [5, 7, [8]]], 21]

class Basepage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self,locator:tuple) -> WebElement:
        self._driver.find_element(*locator)

    def _type(self,locator:tuple,text:str,time:int=10):
        self._wait_until_element_is_visible(time)
        self._find(locator).send_keys(text)

    def _swait_until_element_is_visible(self,locator:tuple,time:int=10):
        wait=WebDriverWait(self._driver,time)
        wait.until(EC.invisibility_of_element_located(locator))
