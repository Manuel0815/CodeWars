import sys
import math
import re

def get_card_strength(card):
    card = re.sub("D|H|C|S", "", card)
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'].index(card)

def get_next_card(cards, tmp_cards):
    tmp_cards.append(cards[0])
    cards.remove(cards[0])
    return cards, tmp_cards

def draw_three_cards(cards, tmp_cards):
    for _ in range(3):
        cards, tmp_cards = get_next_card(cards, tmp_cards)
    return cards, tmp_cards

def play_round(cardsp_1, cardsp_2, tmp_cardsp_1, tmp_cardsp_2, state):
    cardsp_1, tmp_cardsp_1 = get_next_card(cardsp_1, tmp_cardsp_1)
    cardsp_2, tmp_cardsp_2 = get_next_card(cardsp_2, tmp_cardsp_2)

    if get_card_strength(tmp_cardsp_1[-1]) > get_card_strength(tmp_cardsp_2[-1]): # p_1 wins
        cardsp_1 = cardsp_1 + tmp_cardsp_1
        cardsp_1 = cardsp_1 + tmp_cardsp_2
        if len(cardsp_2) == 0:
            state = '1'
    elif get_card_strength(tmp_cardsp_1[-1]) < get_card_strength(tmp_cardsp_2[-1]): # p_2 wins
        cardsp_2 = cardsp_2 + tmp_cardsp_1
        cardsp_2 = cardsp_2 + tmp_cardsp_2
        if len(cardsp_1) == 0:
            state = '2'
    else: # war
        if len(cardsp_1) > 3 and len(cardsp_2) > 3:
            cardsp_1, tmp_cardsp_1 = draw_three_cards(cardsp_1, tmp_cardsp_1)
            cardsp_2, tmp_cardsp_2 = draw_three_cards(cardsp_2, tmp_cardsp_2)
            cardsp_1, cardsp_2, tmp_cardsp_1, tmp_cardsp_2, state = play_round(cardsp_1, cardsp_2, tmp_cardsp_1, tmp_cardsp_2, state)
        else: # draw
            state = 'PAT'

    return cardsp_1, cardsp_2, tmp_cardsp_1, tmp_cardsp_2, state

state = None
rounds = 0
cardsp_1, cardsp_2 = [], []
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    cardsp_1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    cardsp_2.append(cardp_2)

while state is None:
    rounds = rounds + 1
    cardsp_1, cardsp_2, tmp_cardsp_1, tmp_cardsp_2, state = play_round(cardsp_1, cardsp_2, [], [], state)
    
print(state if state == 'PAT' else state + ' ' + str(rounds))