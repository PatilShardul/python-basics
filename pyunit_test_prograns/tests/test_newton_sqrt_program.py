import unittest
from newton_sqrt_program import NewtonSqrt

class TestNewtonSqrt(unittest.TestCase):

    def setUp(self):
        self.newton_sqrt = NewtonSqrt()

    def test_get_user_input(self):
        self.assertRaises(ValueError,self.newton_sqrt.get_user_input) 

if __name__ == "__main__":
    unittest.main()