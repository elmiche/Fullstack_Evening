#lab 12 Guess the Number

import random
x = random.randint(1,10)




# Version 3 
num_tries = 0
while True:
    user_guess = int(input('I\'m thinking of a number (1 through 10), try to guess which: '))
    if user_guess != x:
        num_tries += 1
        print('Try again!')
    if user_guess < x:
        print('too low, try again.')
    if user_guess > x:
        print('too high, try again.')
    elif user_guess == x:
        print(f'Correct! You guessed {num_tries} times.')
        break



# Version 1
# num_tries = 0
# while num_tries <= 9:
#     user_guess = int(input('I\'m thinking of a number (1 through 10), try to guess which: '))
#     if num_tries == 9:
#         print('That\'s 10 tries, sorry but you lose!')
#         break
#     elif user_guess != x:
#         num_tries += 1
#         print('Try again!')
#     elif user_guess == x:
#          print(f'Correct! You guessed {num_tries} times.')
  

