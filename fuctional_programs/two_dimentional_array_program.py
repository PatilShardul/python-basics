two_dimentional_array=[]
def get_cell_values(rows,columns):
    
    for row_index in range(rows):
        row_array=[]
        for column_index in range(columns):
            try:
                row_array.append(int(input(" Enter the user value in cell :")))
            except Exception as e:
                print("Error",e)
        two_dimentional_array.append(row_array)
    print_two_dimentional_array()

def get_rows_columns():
    try:
        rows = int(input("Enter number of Rows : "))
        columns = int(input("Enter number of Columns : "))
        
        get_cell_values(rows,columns)

    except Exception as e:
        print("Enter Valid values ",e)
    
def print_two_dimentional_array():
    for row_index in two_dimentional_array:
        for column_index in row_index:
            print(column_index, end=' ')
    print("\n")                 

get_rows_columns()