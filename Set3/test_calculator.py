import unittest
from calculator import Calculator

class TestCalc(unittest.TestCase):


    def test_add(self):
        a = Calculator(10, 5)
        b = Calculator(-1, -1)
        c = Calculator(-1,1)

        self.assertEqual(a.add(),15)
        self.assertEqual(b.add(), -2)
        self.assertEqual(c.add(), 0)

    def test_sub(self):
        a = Calculator(10, 5)
        b = Calculator(-1, -1)
        c = Calculator(-1, 1)

        self.assertEqual(a.sub(),5)
        self.assertEqual(b.sub(), 0)
        self.assertEqual(c.sub(), -2)

    def test_mul(self):
        a = Calculator(10, 5)
        b = Calculator(-1, -1)
        c = Calculator(-1, 0)

        self.assertEqual(a.mul(), 50)
        self.assertEqual(b.mul(), 1)
        self.assertEqual(c.mul(), 0)

    def test_div(self):
        a = Calculator(10, 5)
        b = Calculator(-1, -1)
        c=Calculator(10,0)

        self.assertEqual(a.div(),2)
        self.assertEqual(b.div(), 1)
        with self.assertRaises(ValueError):
            c.div()


if __name__=='__main__':
    unittest.main()