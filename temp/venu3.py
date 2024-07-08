import unittest
from selenium import webdriver
class Test_venu(unittest.Testcase):
    def test_malli(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com")
if __name__ == "__main":
    unittest.main()