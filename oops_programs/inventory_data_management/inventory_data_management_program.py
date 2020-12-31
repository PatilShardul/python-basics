import json
import math

class InventoryDataManagement:

    def __init__(self):
        pass
    def get_inventory_data(self):
        self.item_total_cost={}
        try:
            inventory_data =  json.load(open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\inventory_data_management\inventory.json"))
            return inventory_data
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
    
    def save_total_value_to_file(self,item_total_cost):
        try:
            with open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\inventory_data_management\inventory_summary.json",'w') as inventory_summary:
                json.dump(item_total_cost, inventory_summary,indent=4)
        except Exception as e:
            print(e)        
    

if __name__ == "__main__":
    
    im = InventoryDataManagement()
    im.calculate_total_value()