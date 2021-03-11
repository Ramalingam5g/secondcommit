import unittest
import adding

class TestAdding(unittest.TestCase):

    def test_adding(self):
        self.assertNotEqual(adding.num1,1)
    def test_adding2(self):
        self.assertEqual(adding.b,5)
    def test_adding3(self):
        self.assertEqual(adding.d,15)

if __name__=="__main__":
    unittest.main()        