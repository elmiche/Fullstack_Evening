#emoticons_lab5.py

import random

eyes_list = [';',':','=','B','X']
nose_list = ['-','~','*']
mouth_list = ['P',']','[',')','(']


emoticon = 0

#final version
while True:
    num_emos = 0
    user_input = input('Would you like to see some emoticons? (y/n): ').lower()
    while num_emos < 5:
        print(random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list))
        num_emos += 1
    if user_input == 'n':
        print('Great, Have a nice day!')
        break


#NOTES & ATTEMPTED Code

#print(random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list))
#add the random.choice module to each list you want to print, the lists should go in order of the face structure


# user_input = input('Would you like to see some emoticons? (y/n): ')
# #asks only once outside of loop
# while user_input != 'n':
        #sometimes trying to figure out the logic of the conditional is harder than just using a while True statement.
#     while emoticon < 5 :
#         print(random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list))
#         emoticon += 1
#     if user_input == 'n':
#         print('Great, Have a nice day!')
#         break
    #incrementing usually at the bottom.
