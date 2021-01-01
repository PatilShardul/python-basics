import json
import math

class InventoryDataManagement:


    def __init__(self):
        pass

    def get_inventory_data(self):
        self.item_total_cost={}
        try:
            self.inventory_data =  json.load(open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\inventory_data_management\inventory.json"))
            return self.inventory_data
        except Exception as e : 
            print("failed to open a file : ",e)    


    def calculate_total_value(self):
        inventory_data=self.get_inventory_data()
        for item_type in inventory_data:
            for item in inventory_data.get(item_type): 
                self.total= float(inventory_data[item_type][item].get("price_per_kg")) * float(inventory_data[item_type][item].get("price_per_kg"))
                self.item_total_cost[item]=self.total
        print(type(self.item_total_cost))
        self.save_total_value_to_file(self.item_total_cost)
    
       
    

    def update_inventory(self):
        inventory_data=self.get_inventory_data()
        
        for item_type in inventory_data:
            print(f"{item_type}")
        
        selected_item_type=input("Enter the desired Item type as given above : ")
        item_type=inventory_data.get(selected_item_type)
        
        for item_name in item_type:
             print(item_name)
        
        selected_item_name=input("Enter the desired Item Name as given above : ")
        details=inventory_data[selected_item_type].get(selected_item_name)
        
        for item_detail,item_value in details.items():
            print(f"property : {item_detail} > Value : {item_value}")

        selected_item_property=input("Enter property you want to update : ")
        # item_property=inventory_data[selected_item_type][selected_item_name].get(selected_item_property) 

        value=input("Enter the value you want to update : ")

        self.inventory_data[selected_item_type][selected_item_name][selected_item_property]=value
        self.save_data() 

    
    def add_inventory_items(self):
    
        new_item_type=input("Enter Item Type : ")
        new_item_name=input("Enter Item Name : ")
        new_price_per_kg=int(input("Enter Price per kg : "))
        new_weight_in_kg=int(input("Enter weight in kg : "))

        items_details={
                    'price_per_kg':new_price_per_kg,
                    'weight_in_kg':new_weight_in_kg
                }
        item_name = {new_item_name: items_details }            

        self.inventory_data[new_item_type]=item_name
        self.save_data() 

    def delete_items(self):
        print(""" do you want to delete 
                  1. item Type
                  2. item 
        """)

        option=int(input("Select option number"))

        if(option==1):

            for item_type in self.inventory_data:
                print(item_type) 
            
            item_type=input("Enter item type value")
            del(self.inventory_data[item_type])

        else:

            for item_type in self.inventory_data:
                print(item_type) 
            item_type=input("Enter item type value")

            for item in self.inventory_data[item_type]:
                print(item)
            item=input("Enter item value")
            del(self.inventory_data[item_type][item])        
        
        self.save_data()        


    def save_data(self):

        try:
            with open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\inventory_data_management\inventory.json",'w') as inventory_summary:
                json.dump(self.inventory_data,inventory_summary,indent=4)
        
        except Exception as e:
            print(e)


    def save_total_value_to_file(self,item_total_cost):
        
        try:
            with open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\inventory_data_management\inventory_summary.json",'w') as inventory_summary:
                json.dump(item_total_cost, inventory_summary,indent=4)
        
        except Exception as e:
            print(e)         



if __name__ == "__main__":
    
    im = InventoryDataManagement()
    im.get_inventory_data()
    print("Please select An Option")
    print("1. get inventory summary")
    print("2. update inventroy")
    print("3. add inventory item")
    print("4. delete inventory item")
    option=int(input())
    if(option == 1):
        im.calculate_total_value()
    elif(option==2):
        im.update_inventory()
    elif(option==3):
        im.add_inventory_items()
    elif(option==4):
        im.delete_items()