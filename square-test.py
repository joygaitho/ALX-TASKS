import unittest

# Import or paste the buggy function here
def square(x):
    # BUG: This should be x * x
    return x + x


class TestSquareFunction(unittest.TestCase):

    def test_valid_input(self):
        """Test correct behavior for valid integers."""
        self.assertEqual(square(5), 25)   # This will FAIL because of the bug
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-4), 16)

    def test_invalid_input(self):
        """Test handling of invalid (non-numeric) input."""
        with self.assertRaises(TypeError):
            square("hello")   # Should raise TypeError

        with self.assertRaises(TypeError):
            square(None)

    def test_float_input(self):
        """Test behavior with float values."""
        self.assertEqual(square(2.5), 6.25)   # Also EXPECTED to FAIL due to bug


if __name__ == '__main__':
    unittest.main(exit = False)
