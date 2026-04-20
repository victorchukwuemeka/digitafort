import unittest 


def multiply(a,b):
    return a * b 


class TestMultiply(unittest.TestCase):
    def testmultiplepositivelll(self):
        self.assertEqual(multiply(2,3),6)

    def testmultiplenegetive(self):
        self.assertEqual(multiply(-3 ,2),-6)


if __name__ == "__main__":
    unittest.main