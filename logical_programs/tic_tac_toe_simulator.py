''' 
  @Author: Shardul Patil
  @Date: 2020-12-27 13:40:38
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-27 13:40:38  
'''

import random
    
board=[]
count=0

#turn_flag is true for player and false for computers chance
turn_flag=True

def draw_board():
    
    print("\n")
    for value in range(0,10):
        board.append(value)
    for index in range(0,3):
        print("",board[index],end=" | ")
    print()    
    for index in range(3,6):
        print("",board[index],end=" | ")
    print()    
    for index in range(6,9):
        print("",board[index],end=" | ")
    print("\n")

#takes player 1 key as input and set player 2 key according to that
def get_player_key():
    global player_key
    try:
        player_key=input("Select Your key/sign from X or O :") 
        set_player_key(player_key)
    except ValueError as e :
        print("Enter valid key",e)
        get_player_key()

# sets player key inserted by the player 1
def set_player_key(key):    
 
    global player_key
    global computer_key
    global turn_flag

    if( player_key == 'X' ):
        computer_key='O'
    elif( player_key == 'O' ):
        computer_key='X'
    else:
        print("Enter valid input key :")
        get_player_key()

    check_turn(turn_flag)


#check which user turn it is
def check_turn(flag):
    
    global turn_flag

    if (flag==True):
        turn_flag=False
        check_index_value(player_key)
    else:
        turn_flag=True
        check_index_value(computer_key)    

#check index value selected by user is not occupies by X or O
def check_index_value(key):
    
    draw_board()
    try:
        index=int(input("Enter the Index value : "))
        if( board[index]!='X' and board[index]!='O' ):
            set_index_value(key,index)
        else:
            print("cell already occupied")
            check_index_value(key)           
    except Exception as e:
        print(e)

#sets values of user key ie. x or o in the board index location    
def set_index_value(key,index):
    global count
    global winner

    board[index]=key
    winner=check_winner()
    
    if(winner=='X' or winner=='O' ):
        count=9
        print("Winner is ",winner)


#check if there is winning combination after every insert
def check_winner():
    if(board[0]==board[1] and board[1]==board[2]):
        return board[0]
    elif(board[3]==board[4] and board[4]==board[5]):
        return board[3]
    elif(board[6]==board[7] and board[7]==board[8]):
        return board[6]
    elif(board[0]==board[3] and board[3]==board[6]):
        return board[0]
    elif(board[1]==board[4] and board[4]==board[7]):
        return board[1]
    elif(board[2]==board[5] and board[5]==board[8]):
        return board[2]
    elif(board[0]==board[4] and board[4]==board[8]):
        return board[0]
    elif(board[2]==board[4] and board[4]==board[6]):
        return board[2]        
    else:
        return None    
        
#start the simulator:

get_player_key()

while(count<8 ):
    count+=1
    check_turn(turn_flag)
draw_board()        
if(winner==None):
    print("Its is a Tie ")

