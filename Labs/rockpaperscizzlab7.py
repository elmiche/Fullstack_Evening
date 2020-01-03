#Rock Papaer Scissors

import random

while True:
    User_choice = input('Choose your weapon: rock, paper or scissors (press "q" to quit): ')
    if User_choice == 'q':
        print('Great! Have a nice day~')
        break
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)


    print(f'The computer chose >>{computer_choice}<<')

    if User_choice == 'rock':
        if computer_choice == 'rock':
            print('It\'s a tie!')
        elif computer_choice == 'paper':
            print('You lose!')
        else:
            print('You win!')
    elif User_choice == 'paper':
        if computer_choice == 'rock':
            print('You win!')
        elif computer_choice == 'paper':
            print('It\'s a tie!')
        else:
            print('You lose!')
    else:
        if computer_choice == 'rock':
            print('You lose!')
        elif computer_choice == 'paper':
            print('You win!')
        else:
            print('It\'s a tie!')

