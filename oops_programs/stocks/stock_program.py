import json
class StockProgram:

    def __init__(self):
        pass
    def get_stock_list(self):
        self.stock_total_cost={}
        try:
            self.stocks_data =  json.load(open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\stocks\stocks_list.json"))
            return self.stocks_data
        except Exception as e : 
            print("failed to open a file : ",e)   
    def calculate_cost(self):

        stock_data=self.get_stock_list()

        for stock_name in stock_data:
                self.total= float(stock_data[stock_name].get("Number of Stocks")) * float(stock_data[stock_name].get("stock_price"))
                self.stock_total_cost[stock_name]=self.total

        self.save_result(self.stock_total_cost)


    def save_result(self,stock_total_cost):
        try:
            with open(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\python_basics\oops_programs\stocks\stocks_report.json",'w') as stock_report:
                json.dump(self.stock_total_cost,stock_report,indent=4)        
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    stock_program = StockProgram()
    stock_program.get_stock_list()
    stock_program.calculate_cost()
