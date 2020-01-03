#passgenlab6.py

#Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

# Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

import random
import string

#these attributes will help make lists
letter = string.ascii_letters
digits = string.digits
punct = string.punctuation
#these are libraries that we converted to string using the imported string module above

#pass_legnth = 5 #this is an Int, we actually don't need it in the final version of code
password_char = letter + digits + punct
random.choice(password_char)
# print(random.choice(letter) + random.choice(digits) + random.choice(punct))
password = '' #password is an empty string
#created a variable, that is an empty string because we haven't added anything to it yet. 

user_password = input('How many characters do you want your password to be?: ')
pass_len = int(user_password)

while len(password) <= pass_len: #we want 5 characters so start with 4 because lists start counting at zero.
    password += random.choice(password_char)



print(password)

#Version2
#Allow the user to enter the value of n, remember to convert its type, as input returns a string.

 

