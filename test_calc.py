import unittest
import calc
class TestCalc(unittest.TestCase): # we run this child class as a Test
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
    def test_subract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), -0)
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)
    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)
        self.assertRaises(ZeroDivisionError, calc.divide, 10, 0) # this test will pass. But if we replace the y value with any number > 0, the test will fail because AssertionError: ZeroDivisionError not raised by divide
       # with self.assertRaises(ZeroDivisionError): here we used a context manager to test exceptions.
           # calc.divide(10, 0)     
if __name__ == "__main__":
    unittest.main() # use exit = False to prevent the code from crash when a test fails
    # unittest.main(exit = False)