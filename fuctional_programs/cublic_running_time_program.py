'''
  @Author: Shardul Patil
  @Date: 2020-12-25 18:59:52
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 18:59:52  
'''

numbers_array=[]

def get_numbers_array():

    try:
        length_of_array=int(input("Enter The Length of the Array"))
    except Exception as e:
        print("Error", e)
    for index in range(length_of_array):
        try:
            numbers_array.append(int(input("Enter the element value")))
        except Exception as e:
            print("Error",e)

    check_addition()

def check_addition():

    triplet_flag=0

    for i in range(len(numbers_array)-2):
        try:
            if (( numbers_array[i] + numbers_array[i+1] + numbers_array[i+2] == 0 )):
                print(numbers_array[i],"+",numbers_array[i+1],"+",numbers_array[i+2],"= 0")
                triplet_flag=1
        except Exception as e:
            print("Error",e)
    if(triplet_flag==0):
        print("No combination Found")    


get_numbers_array()

