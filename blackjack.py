# to do:
# create deck (done)
# create system to distribute cards (done)
# player seating 
# calculations
#   counting total of cards
#   converting ace into 1 or 10 depending if number of cards =2 or >2
#   player total <> dealer total = 1x currency [currency system]
#   total of 21 = 2x currency [currency system]
#   total of 5 cards <21 = 3x currency [curreny system]
#   player loses when total >21 
# player choices
# currency system
# game over screen?

import random as rd
import time as t
import os

fclear=open("hand.txt","w")
fclear.close()

spades=['ace_spades','2_spades','3_spades','4_spades','5_spades','6_spades','7_spades','8_spades','9_spades','10_spades','j_spades','q_spades','k_spades']
clubs=['ace_clubs','2_clubs','3_clubs','4_clubs','5_clubs','6_clubs','7_clubs','8_clubs','9_clubs','10_clubs','j_clubs','q_clubs','k_clubs']
diamonds=['ace_diamonds','2_diamonds','3_diamonds','4_diamonds','5_diamonds','6_diamonds','7_diamonds','8_diamonds','9_diamonds','10_diamonds','j_diamonds','q_diamonds','k_diamonds']
hearts=['ace_hearts','2_hearts','3_hearts','4_hearts','5_hearts','6_hearts','7_hearts','8_hearts','9_hearts','10_hearts','j_hearts','q_hearts','k_hearts']
deck=[spades,clubs,diamonds,hearts]
not_in_deck=[]
cards_temp=[]

k=10
q=10
j=10

def player_count():
    p_count=int(input('How many players will be playing?\n>')) + 1
    return p_count

def distribute(players):
    global cards_temp
    print('Shuffeling...')
    #round1
    for player in range(players):
        shape=rd.choice(deck)
        card=rd.choice(shape)
        cards_temp.append(card)
        not_in_deck.append(card)
    round1=cards_temp
    cards_temp=[]
    
    #round2
    for player in range(players):
        shape=rd.choice(deck)
        card=rd.choice(shape)
        if card in not_in_deck:
            continue
        else:
            cards_temp.append(card)
    round2=cards_temp
    
    #completing hand
    hand_list=[]
    for player in range(players):
        card1=round1[player]
        card2=round2[player]
        hand=card1+'/'+card2+'\n'
        hand_list.append(hand)
    for line in hand_list:
        fhandler=open("hand.txt","a",1)
        fhandler.write(line)
    fhandler.close()
    return

            

players=player_count()
distribute(players)


