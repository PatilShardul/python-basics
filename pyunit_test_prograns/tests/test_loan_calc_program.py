import unittest
from loan_calc_program import LoanCalculator
class TestLoanCalculator(unittest.TestCase):

    def setUp(self):
        self.loan_calc=LoanCalculator()

    def test_get_loan_details(self):
        self.assertRaises(ValueError,self.loan_calc.get_loan_details)

    def test_compute_monthly_payment(self):
        self.assertEqual(self.loan_calc.compute_monthly_payment(5,500,5),9.44)
    
       
    
if __name__ == "__main__":
    unittest.main()
