import unittest
from selenium import webdriver


class searchengineTest(unittest.TestCase):
    def test_Gogle(self):
        self.driver = webdriver.chrome()
        self.driver.get("https://www.google.com/")
        print("tittle of the page", +self.driver.tittle)


if __name__ == "__main__":
