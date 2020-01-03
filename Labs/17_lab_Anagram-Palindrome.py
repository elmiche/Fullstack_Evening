# this is the code for lab 17

#Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.



    #TODO create list string
    #generate iteration variable?



# for letter in word:
#     l_case = word.lower()

#     print(letter)

# def check_palindrome():
#     word = input('Enter a word, let\'s see if it\'s a palindrome: ').lower()
#     letter = ''
#     for i in word: 
#         letter = i + letter 
#     if (word == letter): 
#         print(f'{word} is a palindrome!') 
#     else:
#             return False
    
# print(check_palindrome())

#______________________________________________________
# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal

def check_anagram():
    word1 = input('Enter the first word:').lower()
    word1 = sorted(word1.replace(' ', ''))  
    word2 = input('Enter the second word:').lower()
    word2 = sorted(word2.replace(' ',''))     
    if word1 == word2:
        return True
    else:
        return False

print(check_anagram())
       

   #sort letters

        
   
   