import unittest
from to_binary import ToBinary

class TestToBinary(unittest.TestCase):
    def setUp(self):
        self.to_binary=ToBinary()

    def test_get_decomposed_number(self):
        self.assertRaises(ValueError,self.to_binary.get_decomposed_number,-106)

    def test_get_decomposed_number_type(self):
        self.assertRaises(TypeError,self.to_binary.get_decomposed_number,"hundered")        

if __name__ == "__main__":
    unittest.main()
