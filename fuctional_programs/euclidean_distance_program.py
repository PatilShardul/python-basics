import math

def get_coordinates():
    
    try:
    
        x_coordinate=float(input("Enter X co- ordinate of the point"))
        y_coordinate=float(input("Enter Y co- ordinate of the point"))
        compute_distance(x_coordinate,y_coordinate)
    
    except Exception as e:    
        print("please enter valid co-ordiants")
        get_coordinates(x_coordinate,y_coordinate) 

def compute_distance(x_coordinate,y_coordinate):
     
     try:
         euclidean_distance = math.sqrt(( math.pow(x_coordinate,2) + math.pow(y_coordinate,2) ))
         print("Euclidean Distance ",euclidean_distance)
    
     except Exception as identifier:
         print("Error",e)

get_coordinates()