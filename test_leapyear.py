import unittest
import leapyear

class TestCase(unittest.TestCase):
    #def test1(self):
     #   self.assertEqual(leapyear.leapyear(200), "True")
    #def test2(self):
     #   self.assertEqual(leapyear.leapyear(2000), "False")
    #def test3(self):
     #   self.assertEqual(leapyear.leapyear(2000), "True")
    def test4(self):
        self.assertEqual(leapyear.leapyear(2000), "This is a leap year")
    def test5(self):
        self.assertEqual(leapyear.leapyear(2001), "This is not a leap year")

if __name__ == '__main__':
    unittest.main()