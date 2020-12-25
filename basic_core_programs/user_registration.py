'''
  @Author: Shardul Patil
  @Date: 2020-12-25 11:22:37
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 11:22:37  
'''
import re

user_name_valid_flag=False

while(user_name_valid_flag==False):
    try:
        user_name=input("Please Enter your User Name : ")
        
        if(re.search('^[a-zA-Z0-9]{3,}',user_name)):
            user_name_valid_flag==True
            print("Welcome",user_name,"How are you ?")
        else:
            print("please Enter Valid user Name ")
    
    except Exception as e :
        print("Error Occured" , e)

