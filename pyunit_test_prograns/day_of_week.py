''' 
  @Author: Shardul Patil
  @Date: 2020-12-30 12:27:43
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-30 12:27:43  
'''
class DayOfWeek:
    def __init__(self):
        
        self.day=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    def get_date(self):
        try:
            month = int(input("Enter the Month number: "))
            date = int(input("Enter the Date : "))
            year = int(input("Enter the Year : "))
        except ValueError as e:
            print("Give Valid Input Value error : ",e)
            self.get_date()
        if (( month<=0 or month > 12) or ( date <= 0 or date > 31 )):
            raise ValueError("Enter month between (1,12) and date between(1,31)")     
        self.get_day(month,date,year)

    def get_day(self,m,d,y):
        y0 =  y - ( 14 - m ) // 12
        x = y0 + ( y0 // 4 ) - ( y0 // 100 ) + ( y0 // 400 )
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7
        print(f"Day on : {d}/{m}/{y} is {self.day[d0]}")

if __name__ == "__main__":
    day_of_week=DayOfWeek() 
    day_of_week.get_date()