import json

class AddressBookManager:

    def __init__(self):
        pass

    
    def get_address_book_data(self):
        try: 
            self.address_book_data=json.load(open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\inventory_data_management\address_book\address_book.json"))        
        except Exception as e :
            print("Error Unable to open the file : ",e)


    def get_options(self):
        
        print("Please select An Option")
        print("1. add Address")
        print("2. update Address")
        print("3. deleteAddress")
        
        option=int(input())
        
        if(option==1):
            address_book.add_address()
        elif(option==2):
            address_book.update_address()
        elif(option==3):
            address_book.delete_address()
        else:
            print("Select Valid option")
            self.get_options()


    def delete_address(self):
        
        print("do you want to delete") 
        print("1. Location")
        print("2. Person")
        try:
            option=int(input("Select option number"))
        except Exception as e:
            print("Enter Valid option",e)
            self.delete_address()

        if(option==1):

            for location in self.address_book_data:
                print(location) 
            try:
                location=input("Enter Location :")
                del(self.address_book_data[location])
            except Exception as e :
                print("Error : Unable to delete location : ",e)
                self.delete_address()
        
        else:

            try:
                for location in self.address_book_data:
                    print(location) 
                location=input("Enter Location value")

                for person in self.address_book_data[location]:
                    print(person)
                person=input("Enter person name:")
                del(self.address_book_data[location][person])
            except Exception as e:
                print("Unable to delete Person",e)
                self.delete_address()

        self.save_address_book()
            
    def update_address(self):
        
        for location in self.address_book_data:
            print(f"{location}")
        
        selected_City=input("Enter City Name  : ")
        location=self.address_book_data.get(selected_City)
        
        for person in location:
             print(person)

        selected_person=input("Enter Person name : ")
        person_details=self.address_book_data[selected_City].get(selected_person)
        
        for detail_key,detail_value in person_details.items():
            print(f" {detail_key} : {detail_value}")

        selected_person_property=input("Enter person property you want to update : ")
        
        value=input("Enter the value you want to update : ")
        self.address_book_data[selected_City][selected_person][selected_person_property]=value
        self.save_address_book()
        
    def add_address(self):
        print("1 . Add new location and person")
        print("2. Add new person")
        option=int(input())
        if(option==1):
            try:
                new_city=input("Enter City Name : ")
                new_person=input("Enter Person Name : ")
                new_phone=int(input("Enter Phone No. : "))
                new_address=input("Enter new Address : ")
                new_pincode=int(input("Enter Pincode : "))
            except Exception as e:
                print("Please Provide Valid values:")
                self.add_address()
            person_details={
                    'phone':new_phone,
                    'address':new_address,
                    'pincode':new_pincode
                    }
            person_name= {
                new_person: person_details 
                }
                
            self.address_book_data[new_city]=person_name

        else:
            
            for location in self.address_book_data:
                print(f"{location}")
            try:    
                selected_City=input("Enter City Name  : ")

                new_person=input("Enter Person Name : ")
                new_phone=int(input("Enter Phone No. : "))
                new_address=input("Enter new Address : ")
                new_pincode=int(input("Enter Pincode : "))
            except Exception as e:
                print("Please eprovide Valid values")
                self.add_address()    
            person_details={
                    'phone':new_phone,
                    'address':new_address,
                    'pincode':new_pincode
                    }
            person_name= {
                new_person: person_details 
                }     
            self.address_book_data[selected_City][new_person]=person_details
            
            print(self.address_book_data)
        self.save_address_book() 
    
    
    def save_address_book(self):
        try:
            with open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\inventory_data_management\address_book\address_book.json",'w') as address_book:
                json.dump(self.address_book_data,address_book,indent=4)
        
        except Exception as e:
            print(e)




if __name__ == "__main__":
    address_book = AddressBookManager()
    address_book.get_address_book_data()
    address_book.get_options()
