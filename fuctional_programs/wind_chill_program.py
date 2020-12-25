'''
  @Author: Shardul Patil
  @Date: 2020-12-25 21:23:06
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 21:23:06  
'''
import math


def get_v_t_variables():
    try:
        v=float(input("Enter The Value of V : "))
        t=float(input("Enter The Value of T : "))
        if( t < 50 and v < 120 and v > 3):
            compute_wind_chill(v,t)
        else:
            print("value of t should be less than 50 and value  v should should be between 3 to 120 ")
            get_v_t_variables()
    except Exception as e :
        print("Please enter Valid numeric values for v and t",e)
        get_v_t_variables()        


def compute_wind_chill(v,t):

    w = round(( 35.74 + 0.6215 * t + ( 0.4275 * t - 35.75 ) * math.pow(v,0.16) ),2) 
    print("wind chill factor is : ",w)


get_v_t_variables()


