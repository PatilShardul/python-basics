'''
  @Author: Shardul Patil
  @Date: 2020-12-25 16:21:54
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 16:21:54  
'''

import math

max_limit_number=int(input("Enter The Number to Compute Prime Factorization "))
i=0
prime_numbers=[]

for i in range(i*i, max_limit_number):
   # all prime numbers are greater than 1
   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           prime_numbers.append(i)

while( max_limit_number > 1 ):
    for number in prime_numbers:
        if ( max_limit_number % number == 0 ):
            print(number)
            max_limit_number=max_limit_number/number
            break
        else:
            continue            

