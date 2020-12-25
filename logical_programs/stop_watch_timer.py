import datetime

def start_timer():
    try:
        start_time=datetime.datetime.now()
        input("Timer Started , Press Enter to Stop the Stop : ")
        stop_timer(start_time)
    except Exception as e :
        print(e)


def calculate_time_difference(start_time,stop_time):
    print( stop_time - start_time )

def stop_timer(start_time):
    try:
        stop_time=datetime.datetime.now()
        calculate_time_difference(start_time,stop_time)
    except Exception as e :
        print(e)


start_timer()


