import unittest
from binary import BinaryToDecimal
class TestBinary(unittest.TestCase):
    def setUp(self):
        self.binary_to_decimal=BinaryToDecimal()
    def test_get_user_input(self):
        self.assertRaises(ValueError,self.binary_to_decimal.get_user_input)


if __name__ == "__main__":
    unittest.main()