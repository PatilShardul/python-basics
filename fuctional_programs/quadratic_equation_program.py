'''
  @Author: Shardul Patil
  @Date: 2020-12-25 20:50:53
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 20:50:53  
'''
import math

print("Quadratic Equation is a ( x * x ) + b * x + c = 0 ")

def get_quadratic_equation_constant_values():
    try:
        a=int(input("Enter the value for a : "))
        b=int(input("Enter the value for b : "))
        c=int(input("Enter the value for c : "))

        compute_determinant(a,b,c)
    
    except Exception as e:
        print("please Enter valid value for a,b,c",e)
        get_quadratic_equation_constant_values()

def compute_determinant(a,b,c):
    try:
        determinant=( math.pow(b,2) - 4*a*c )
        compute_roots(determinant,a,b,c)  
    except Exception as e:
        print(e)
        get_quadratic_equation_constant_values()

def compute_roots(determinant,a,b,c):
    try:
    
        if(determinant<0):
            print("No real roots")
        elif(determinant==0):
            root=(-b/(2*a))
            print("Only one Root : ",root)
        elif(determinant>0):
            root=float(( ( -b + math.sqrt( determinant )) / ( 2 * a ) ))
            print("first root : ",root)
            root=float(( ( -b - math.sqrt( determinant )) / ( 2 * a ) ))
            print("second root : ",root )
        
    except Exception as e :
        print(e)
        get_quadratic_equation_constant_values()                 

get_quadratic_equation_constant_values()  