import unittest
from selenium import webdriver
class Test_venu(unittest.TestCase):
    def test_venu(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com")
        #titleofwebpage=webdriver.title
        #self.assertTrue(titleofwebpage=="Google")
if __name__ == "__main__" :
    unittest.main()




