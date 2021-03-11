import unittest
import average_noraml_way

class TesAverage(unittest.TestCase):
    def test_average_valid(self):
        out= average_normal_way([10,10,10])
        self.assertEqual(out,10,'failed')

if __name__=="__main__":
    unittest.main()