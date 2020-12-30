''' 
  @Author: Shardul Patil
  @Date: 2020-12-30 12:28:18
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-30 12:28:18  
'''
import math

class ToBinary:

    def __init__(self):
        pass
    
    def get_decomposed_number(self,number): 
        if( number < 0 ):
            raise ValueError("Number Should Be greater than zero : ")
        if type(number) not in [int,float]:
            raise TypeError("Enter Valid interger or float number : ")


        decomposed_index_position = [] 

        print ("Decomposed is {number} : ", end=" ") 
        while (number > 0): 
            decomposed_index_position.append(int(number % 2)) 
            number = int(number / 2) 

        for i in range(0, len(decomposed_index_position)): 
            if (decomposed_index_position[i] == 1): 
                print (math.pow(2,i), end = " ") 
                if (i != len(decomposed_index_position) - 1): 
                    print ("+ ", end = "") 
        print ("\n")

if __name__ == "__main__":
    to_binary = ToBinary()
    to_binary.decomposed_number(106)