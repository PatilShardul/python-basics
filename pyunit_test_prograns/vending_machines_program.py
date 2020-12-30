''' 
  @Author: Shardul Patil
  @Date: 2020-12-30 12:28:13
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-30 12:28:13  
'''
from collections import OrderedDict

class VendingMachine :
    
    def __init__(self):
        self.denominations_count = OrderedDict()
        self.denominations_count[1] = 10
        self.denominations_count[2] = 10
        self.denominations_count[5] = 10
        self.denominations_count[10] = 10
        self.denominations_count[50] = 10
        self.denominations_count[100] = 10
        self.denominations_count[500] = 10
        self.denominations_count[1000] = 10
        self.total_amount=0
        # for value in self.denominations_count.values()
        #     self.total_amount=total_amount+value         
    
    
    def get_user_input_amount(self):
    
        try:
            user_amount = int(input("Enter the Amount : "))
        except Exception as e:
            print("Enter Valid Amount values in Numeric",e)
            self.get_user_input_amount()
        if(user_amount<=0):
            raise ValueError("Enter Number Greater than 0")
        self.check_max_denomination(user_amount)        
    def update_denomination_count(self,key,value,user_amount):
        self.denominations_count[key]=value
        print(f"{key} : {10-value}")
        self.check_max_denomination(user_amount) 

    def get_dinomination(self,max_demonination,user_amount):
        max_demonination_count = user_amount // max_demonination
        value=self.denominations_count[max_demonination]
        if ( max_demonination_count <= value and user_amount != 0):
            value -= max_demonination_count
            user_amount = user_amount % max_demonination 
            self.update_denomination_count(max_demonination,value,user_amount)

        
    def check_max_denomination(self,user_amount):
        try:
            for key in self.denominations_count.keys():
                if ( user_amount < key ) :
                    break
                max_denomination=key
            self.get_dinomination(max_denomination,user_amount)              
        except Exception as e:
            pass                
                    


    
def dispatch_money(self):
    pass

if __name__ == "__main__":   
    vm = VendingMachine()
    vm.get_user_input_amount()