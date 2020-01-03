#this is lab 19


# three playing cards from -->> (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).

def card_play(card):
    if card == 'A':
        return 1
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    else:
        return int(card)


def black_jack():
    card_1 = input('what is the first card?: ')
    card_2 = input('what is the second card?: ')
    card_3 = input('what is the third card?: ')

    total = card_play(card_1) + card_play(card_2) + card_play(card_3)


    if total < 17:
        print('hit!')
    elif total < 21:  
        print('stay!')
    elif total == 21:
        print('blackjack!')
    else:
        print('busted!')

black_jack()



# this is where you add the user inputs cards up for the total and then go to the if loop for advice
    # if card_1 == 'A' #and total <= 11:
    #     total += 10
        
    # if card_2 == 'A' #and total <= 11:
    #     total += 10
    # if card_3 == 'A' #and total <= 11:
    #     total += 10
#ADVICE LOOP - now this is the conditions for the next actions based on the total, blackjack you want to hit 21.         
   

