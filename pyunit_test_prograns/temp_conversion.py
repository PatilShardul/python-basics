''' 
  @Author: Shardul Patil
  @Date: 2020-12-30 12:28:02
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-30 12:28:02  
'''

import math

class TemperatureConvert:

    def __init__(self):
        pass

    def get_temperature(self):
        try:
            temp=float(input("Enter Temperature value you want ot convert"))
            return temp
        except (ValueError,TypeError) as e:
            print("Enter Temperatue in int ot float format :",e)
            self.get_temperature()

    def celsius_to_fahrenheit(self,temp):
        
        if type(temp) not in [int,float]:
            raise TypeError("Enter Value in int or float format")
        else:
            temp_in_fahrenheit = (temp * 9/5) + 32    
            print(f"{temp} in fahrenheit is :{temp_in_fahrenheit}")


    def fahrenheit_to_celsius(self,temp):
        try:
            temp_in_celsius = ( temp - 32 ) * ( 5 / 9 )    
            print(f"{temp} in celcius is :{temp_in_celsius}")    
        except Exception as e:
            pass 

if __name__ == "__main__":
    print("Welcome to Temperature converter Program :\nchooose one option")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    option=input()
    temperature_convert=TemperatureConvert()
    try:
        temp=temperature_convert.get_temperature()
        
        if(option == '1'):
            temperature_convert.celsius_to_fahrenheit(temp)
        else:
            temperature_convert.fahrenheit_to_celsius(temp)
    except Exception as e:        
        pass