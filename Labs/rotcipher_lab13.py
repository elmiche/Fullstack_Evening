# LAB 13 ROT Cipher



#Version 2

import string
#user input - message to encode
def user_str(message): 
    return input(message).lower()

# ROT = 'nopqrstuvwxyzabcdefghijklm'

#function for rotation specifications
def user_rotation(rot_str, rotation):
    user_ROT = ''
    for letter in rot_str:
        index = string.ascii_lowercase.find(letter)
        user_ROT += string.ascii_lowercase[(index + rotation) %26 ]
    return user_ROT

def encryption_code():
    while True:
        rotation = input('enter number of rotations (enter \'quit\' to exit): ')
        if rotation == 'quit':
            print('Great! Have a nice day')
            break
        user_message = user_str('Type a secret message for me to encrypt or \'quit\': ') 
        encryption_message = user_rotation(user_message, int(rotation))
        print(encryption_message)
encryption_code()



#version 1 code

# user_str = input('Type a secret message for me to encrypt: ')
# ROT = 'nopqrstuvwxyzabcdefghijklm'

# rotated = ''
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for letter in user_str:
#     index = alphabet.find(letter)
#     rotated += ROT[index]
# print(rotated)