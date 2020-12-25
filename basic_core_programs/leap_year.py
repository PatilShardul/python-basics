'''
  @Author: Shardul Patil
  @Date: 2020-12-25 12:43:29
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 12:43:29  
'''
try:
    
    year=int(input("Enter A year :"))

    if ( year % 400 == 0) or (( year % 4 == 0) and ( year % 100 != 0 ) ):
        print(year,"is a Leap Year.")
    else:
        print(year," is not a Leap Year.")
except Exception as e :
    print("Enter a year in valid integer format",e)

        