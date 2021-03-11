import unittest
class TestDemo(unittest.TestCase):
    def setup(self):
        print("setup is execution")
    def test_ram(self):
        print("test is execution")
    def test_ram2(self):
        print("test is execution")
    def tearDown(self):
        print("tearDown is execuion")
unittest.main()