import unittest
import check

class TestChecking(unittest.TestCase):
    def test_checking(self):
        self.assertEqual(check.a,22)
    def test_checking(self):
        self.assertNotEqual(check.b,22)



if __name__=="__main__":
    unittest.main()       