''' 
  @Author: Shardul Patil
  @Date: 2020-12-30 12:27:54
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-30 12:27:54  
'''
import math
class NewtonSqrt:
    def __init__(self):
        pass
    
    def get_user_input(self):
        try:
            c=int(input("Enter number to find a square root: "))
        
        except Exception as e :
            print("Enter Valid interger",e)    
            self.get_user_input()
        if( c<0 ):
            raise ValueError("Enter Positive Interger")
        self.calculate_sqrt(c)    

    def calculate_sqrt(self, c):
        t=c
        epsilon=1e-15
        try:
            while( abs(t - c / t) > epsilon * t ):
                t = ( c / t + t) / 2
            print(f"square root of {c} is {t}")    
        except Exception as e:
            print(e)
if __name__ == "__main__":
    newton_sqrt=NewtonSqrt()
    newton_sqrt.get_user_input()