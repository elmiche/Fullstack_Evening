#lab 14 pick6_lab14.py


from random import randint 


def pick_6():
    number_list = []
    for i in range(6):
        number_list.append(randint(1,99))        #this will add 6 random int to number_list between 1 - 99
    return number_list

#matching numbers function
def track_matches(pick_6):
    user_ticket = pick_6()
    winnin_ticket = pick_6()
    match_count = 0
    for i in range(len(user_ticket)):
        if user_ticket[i] == winnin_ticket[i]:
            match_count += 1
    return match_count

#If you match numbers
balance = 0
def match_rewards(match_count, balance):
    balance -= 2                            # $2 a ticket
    if match_count == 1:
        balance += 4
    elif match_count == 2:
        balance += 7
    elif match_count == 3:
        balance += 100
    elif match_count == 4:
        balance += 50000
    elif match_count == 5:
        balance += 1000000
    elif match_count == 6:
        balance += 25000000
    else:
        return balance
    return(match_count)
print(match_rewards(track_matches(pick_6), balance))













# def play_6(match_tracker, rewards):
#     matches = match_tracker()
#     rewards = rewards(matches)
#     print(rewards)
#     print('playing Pick 6') #use this to play 1 game of Pick6

# def main(play_6):
#     loops = 0
#     while loops <= 9: #should be 999999
#         play_6()
#         loops += 1



#call all these functions in the right order, fingers crossed ~