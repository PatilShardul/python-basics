'''
  @Author: Shardul Patil
  @Date: 2020-12-25 13:07:38
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 13:07:38  
'''
real_time_power=0

try:
    
    MAX_POWER_VAL=int(input("Enter the Max power value which is less than 31 : "))
    print("\n Power of 2 table : \n")
    while ( real_time_power <= MAX_POWER_VAL ) and ( MAX_POWER_VAL <= 31 ):
        print("2 ^",real_time_power,"=",(2**real_time_power))
        real_time_power+=1

except Exception as e:

    print("Please Enter a Valid interger power less than 31",e)    