''' 
  @Author: Shardul Patil
  @Date: 2020-12-30 12:27:34
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-30 12:27:34  
'''
import math 
class BinaryToDecimal:

    def __init__(self):
        self.binary_list=[]
        self.first_nibble=[]
        self.last_nibble=[]
        self.swaped_binary=[] 

    def get_user_input(self):
            
            try:
                decimal_number=int(input("Enter a decimal Number less than 128 : "))
            except TypeError as e:
                print("Enter Value as interger : ",e)

            if decimal_number < 0  and decimal_number < 128:
                raise ValueError("number should be greater than 0 and less than 128")
            self.get_binary(decimal_number)

        
    def get_binary(self,decimal_number):

        for index in range(0,8):
            self.binary_list.append(decimal_number%2)
            decimal_number//=2
            print(self.binary_list[index],end=" ")
        
        self.get_last_nibble()
        self.get_first_nibbles()           
        self.get_decimal()

    def get_first_nibbles(self):
        for index in range(0,4):
            self.swaped_binary.append(self.binary_list[index])
            

    def get_last_nibble(self):
        for index in range(4,8):
            self.swaped_binary.append(self.binary_list[index])

    def get_decimal(self):
        decimal=0
        for index in range(0,8):
            if(self.swaped_binary[index]!=0):
                decimal += math.pow(2,index) 
        print(decimal)

if __name__ == "__main__":
    binary_to_decimal = BinaryToDecimal()
    binary_to_decimal.get_user_input()    

