import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.leapyear(200), "True")
   

if __name__ == '__main__':
    unittest.main()