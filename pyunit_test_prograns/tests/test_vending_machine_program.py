import unittest
from vending_machines_program import VendingMachine

class TestVendingMachine(unittest.TestCase):

    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_get_user_input_amount(self):
        self.assertRaises(ValueError,self.vending_machine.get_user_input_amount)

if __name__ == "__main__":
    unittest.main()


