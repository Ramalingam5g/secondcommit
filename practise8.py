import unittest

def sum(a,b,c):
    return a+b+c

class CodeTest(unittest.TestCase):
    def setUp(self):
        self.a=20
        self.b=23
        self.c=22
    def test_add_func(self):
        result=sum(self.a,self.b,self.c)
        self.assertEqual(result,self.a+self.b+self.c)
        print(result)

    def test_add_func2(self):
        result=sum(self.b,self.c,self.a)
        self.assertEqual(result,self.b+self.c+self.a)
        print(result)

            

if __name__ == "__main__":
    unittest.main()
