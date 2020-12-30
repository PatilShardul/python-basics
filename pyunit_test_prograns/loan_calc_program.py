''' 
  @Author: Shardul Patil
  @Date: 2020-12-30 12:27:49
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-30 12:27:49  
'''
import math
class LoanCalculator:
    def __init__(self):
        pass
    
    def get_loan_details(self):
        
        try:
            years=float(input("enter the number of years : "))
            principal=float(input("Enter the Principal Amount : "))
            compound_intrest=float(input("Enter The Compund rate of interest : "))
        except Exception as e :
            print(e)
        
        if years <= 0 or principal <= 0 or compound_intrest <= 0 : 
                raise ValueError("Enter Valid year,principal Compuond interset")
        self.compute_monthly_payment(years,principal,compound_intrest)       
    
    def compute_monthly_payment(self,years,principal,compound_intrest):
        n=years*12
        r=compound_intrest/( 12*100 )
        monthly_payment= round(( principal * r ) / ( 1 - math.pow( ( 1 + r) , (-n)) ),2)
        print(monthly_payment)
        return monthly_payment


if __name__ == "__main__":
    
    loan_calculator = LoanCalculator()
    loan_calculator.get_loan_details()

