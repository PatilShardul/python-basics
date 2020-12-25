'''
  @Author: Shardul Patil
  @Date: 2020-12-25 11:43:25
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 11:43:25  
'''

import random

number_of_heads=0
number_of_tails=0
flip_count=0
heads_percentage=0
tails_percentage=0

try:

    TOTAL_COIN_FLIP=int(input("Enter the total number of coin flip expected : "))     
    
    while (( TOTAL_COIN_FLIP > 0 ) && ( flip_count <= TOTAL_COIN_FLIP )) :  
        
        flip_count=+1
        result=random.uniform(0,1)
    
        if(result>0.5):
            number_of_heads=+1
        else:
            number_of_tails=+1

    heads_percentage=((number_of_heads/TOTAL_COIN_FLIP)*100)
    tails_percentage=((number_of_tails/TOTAL_COIN_FLIP)*100)

except Exception as Error:
    print(Error)

finally:
    print("Heads Percentage is :" ,heads_percentage,"%")
    print("Tails Percentage is :",tails_percentage,"%")                    
