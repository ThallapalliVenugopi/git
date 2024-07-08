from selenium import webdriver
import pytest
from selenium import webdriver


@pytest.fixture()
def driver_ob():
    print("creating chrome browser")
    my_driver = webdriver.Chrome()

    # my_driver.implicitly_wait(10)
    yield my_driver

    print("closing chrome Driver ")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: type1 or type2"
    )
