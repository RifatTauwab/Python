import unittest
from leap import leapyear
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(leapyear(5),True)
    def test_2(self):
        self.assertEqual(leapyear(2010),True)
    def test_3(self):
        self.assertEqual(leapyear(400),True)
    def test_4(self):
        self.assertEqual(leapyear(2100),True)
    def test_5(self):
        self.assertEqual(leapyear(2000),True)
if __name__ == '__main__':
    unittest.main()
