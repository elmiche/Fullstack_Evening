#Magic 8-Ball

import random
#this imports the random module
#user_input = input('Ask me a question, or type DONE to leave Magic 8 Ball: ')

while True:
    #STARTS HERE - while loop
    user_input = input('Ask me a question, or type DONE to leave Magic 8 Ball: ')
    magic_phrases = [' Try again','Good Plan','I wouldn\'t', 'sounds risky', 'Yes, Definitely.','I wouldn\'t advise that']

    user_shake = random.choice(magic_phrases)
    #This variable stores the random choice method's random selection from the magic_phrases list
    print(f"Magic 8 Ball says: {user_shake} ")
    #This is an f-string
    if user_input == 'DONE':
        print('Great, Have a nice day!')
        break
    #ENDS HERE - while loop
#Verion 2 with While loops and option to exit
