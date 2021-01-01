import random
class CardDeck:
    def __init__(self):
        self.cards_type=["HEART","SPADES","DIAMONDS","CLUBS"]
        self.cards_numbers=[2,3,4,5,6,7,8,9,10,"JACK","QUEEN","KING","ACE"]
        self.player_one_cards={"HEART":[],"SPADES":[],"DIAMONDS":[],"CLUBS":[]}
        self.player_two_cards={"HEART":[],"SPADES":[],"DIAMONDS":[],"CLUBS":[]}
        self.player_three_cards={"HEART":[],"SPADES":[],"DIAMONDS":[],"CLUBS":[]}
        self.player_four_cards={"HEART":[],"SPADES":[],"DIAMONDS":[],"CLUBS":[]}
    
    def get_card_type(self):
        card_type=self.cards_type[random.randint(0,3)]
        return card_type
    def get_card_number(self):
        card_number=self.cards_numbers[random.randint(0,12)]
        return card_number
    def check_card_exists(self,player_number,card_type,card_number):

        if(player_number == 1):
            for key,number_list in self.player_one_cards.items():
                if( key == card_type and card_number in number_list):
                    return True
                else:
                    return False
        elif(player_number == 2):
            for key,number_list in self.player_one_cards.items():
                if( key == card_type and card_number in number_list):
                    return True
                else:
                    return False
        elif(player_number == 3):
            for key,number_list in self.player_one_cards.items():
                if( key == card_type and card_number in number_list):
                    return True
                else:
                    return False
        elif(player_number == 4):
            for key,number_list in self.player_one_cards.items():
                if( key == card_type and card_number in number_list):
                    return True
                else:
                    return False                         

    def set_player_card(self):
    
        card_type=self.get_card_type()
        card_number=self.get_card_number()
        
        player_number=2
        card_exist=self.check_card_exists(player_number,card_type,card_number)
        if(card_exist == False):
            self.player_two_cards[card_type].append(card_number)
        card_type=self.get_card_type()
        card_number=self.get_card_number()
        
        player_number=3
        card_exist=self.check_card_exists(player_number,card_type,card_number)
        if(card_exist == False):
            self.player_three_cards[card_type].append(card_number)
        card_type=self.get_card_type()
        card_number=self.get_card_number()
        
        player_number=4
        card_exist=self.check_card_exists(player_number,card_type,card_number)
        if(card_exist == False):
            self.player_four_cards[card_type].append(card_number)
        card_type=self.get_card_type()
        card_number=self.get_card_number()
        
        player_number=1
        card_exist=self.check_card_exists(player_number,card_type,card_number)
        if(card_exist == False):
            self.player_one_cards[card_type].append(card_number)
    
    def get_player_cards(self):
        print("Player 1 cards : ","\n")
        print(self.player_one_cards,"\n")
        print("Player 2 cards : ","\n")
        print(self.player_two_cards,"\n")
        print("Player 3 cards : ","\n")
        print(self.player_three_cards,"\n")
        print("Player 4 cards : ","\n")
        print(self.player_four_cards,"\n")
    



if __name__ == "__main__":
    card_deck=CardDeck()
    round_count=1
    while(round_count <=9):
        card_deck.set_player_card()    
        round_count+=1
    card_deck.get_player_cards()    