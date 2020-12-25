'''
  @Author: Shardul Patil
  @Date: 2020-12-25 22:13:37
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2020-12-25 22:13:37  
'''
import random

BET_AMOUNT=1

goal_amount=0
stake_amount=0
total_bets=0


def get_stake_goal_amount():

    try:
        stake_amount=int(input("Enter The Stake Amount : "))
        goal_amount=int(input("Enter The Goal Amount : "))
        total_bets=int(input("Enter The total bets : "))
        start_betting(stake_amount,goal_amount,total_bets)
    except Exception as e:
        print("Error",e)
        get_stake_goal_amount()


def start_betting(stake_amount,goal_amount,total_bets):
    no_of_bets=0
    no_of_wins=0
    no_of_loss=0
    while( stake_amount <= goal_amount and stake_amount >= 0 and no_of_bets < total_bets):    
        no_of_bets+=1
        bet_result=random.uniform(0,1)
        
        if(bet_result > 0.5):
            stake_amount+=BET_AMOUNT
            no_of_wins+=1
        else:
            stake_amount-=BET_AMOUNT
            no_of_loss+=1
    try:
        print("number of wins : ",no_of_wins)
        print("percentage of wins : ",((no_of_wins/total_bets)*100))
        print("percentage of loss : ",((no_of_loss/total_bets)*100))
    except Exception as e:
        print("Error",e)
        get_stake_goal_amount()


get_stake_goal_amount()