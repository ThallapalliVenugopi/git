import unittest
class Testvenu(unittest.TestCase):

    @classmethod
    def setup(self):
        print("this is c login test")
    @classmethod
    def tearDown(self):
        print("This is c logut test")

    def test_search(self):
        print("i am venu gopi")
    def test_malli(self):
        print("malli is fine")
if __name__ == "__main__":
    unittest.main()