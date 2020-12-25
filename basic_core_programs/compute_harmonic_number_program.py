'''
  @Author: Shardul Patil
  @Date: 2020-12-25 13:24:47
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 13:24:47  
'''

HARMONIC_NUMERATOR=1
real_time_dinominator=1
harmonic_value=0

try:
    
    max_harmonic_limit = int(input("Enter the limit for Nth Harmonic number : "))

    while ( real_time_dinominator <= max_harmonic_limit and max_harmonic_limit > 0 ):
        harmonic_value=harmonic_value+(HARMONIC_NUMERATOR/real_time_dinominator)
        real_time_dinominator+=1
        print(harmonic_value)

except Exception as e :
    print("Enter valid interger value",e)
