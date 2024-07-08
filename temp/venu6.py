import unittest
from selenium import webdriver
class Test_name(unittest.TestCase):
    def test_name(self):
        driver=webdriver.Chrome()
        driver.get("https://www.facebook.com/")
        titleofthepage=driver.title
        self.assertEqual("Facebook – log in or sign up",titleofthepage,"this test is failed")
if __name__ == "__main__":
    unittest.main()