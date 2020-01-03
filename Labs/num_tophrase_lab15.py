


num = int(input('enter a number between 0 and 999: '))

def converter():
    tens_digit = num % 100      #floor division, is true division leaves NO remainder, we need extract the remainder for tens_digit
    ones_digit = num % 10       #modulus leaves a remainder behind. This returns the ones_digit remainder, extract it!
    hundreds_place = num // 100
    
   

    ones = [
        '',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten' 
        ]

    teens = [
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eightteen',
        'nineteen'
        ]

    tens = [
        '',
        'ten',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety',
        ]

    hundreds = [
        '',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten' 
        ]

#     print(tens_digit, ones_digit, hundreds_place, tens[ones_digit])
#     word_num = ''
#     if hundreds_place:
#         if tens_digit == 0 and ones_digit:
#             word_num = f'{hundreds[hundreds_place]} hundred - {ones[ones_digit]}'
#         elif tens_digit == 1:
#             word_num = f'{hundreds[hundreds_place]} hundred - {teens[tens_digit]}'
#         elif tens_digit > 1:
#             word_num == f'{hundreds[hundreds_place]} hundred - {tens[tens_digit]}'
#         else:
#             word_num == f'{hundreds[hundreds_place]}'
#         return word_num
#     elif tens_digit != 0:
#         if tens_digit == 1:
#             word_num = teens[tens_digit]
#             return word_num
#         elif tens_digit > 1:
#             word_num = tens[tens_digit]
#             return word_num
#         return word_num
#     else:
#         word_num = ones[ones_digit]
#         return word_num


# print(converter())




#first attempt, buggy af
    print(tens_digit, ones_digit, hundreds_place, tens[ones_digit])
    
    if hundreds_place != 0 and tens_digit == 0: 
        word_num = f'{ones[hundreds_place]} hundred and {ones[ones_digit]}'
    elif hundreds_place != 0 and tens_digit != 1:                             #hundred and tens place
        word_num = f'{ones[hundreds_place] } hundred and {teens[ones_digit]}'   
    elif hundreds_place != 0 and tens_digit == 1:                           #hundreds with teens place
        word_num = f'{ones[hundreds_place]} hundred - {teens[ones_digit]}'  
    elif hundreds_place != 0 and ones_digit:                                #hundred and ones place
        word_num = f'{ones[hundreds_place]} hundred - {ones[tens_digit]}' #TODO 
    elif hundreds_place != 0:                                               #perfect hundreds place
        word_num = f'{ones[ones_digit]} hundred'
    elif tens_digit == 0 and ones_digit:                                    #one's place
        word_num = ones[ones_digit]
    elif tens_digit == 1:                                                   #teens require num in ten's place, use the ones_digit var to extract remainder, set as index
        word_num = teens[ones_digit]
    # elif tens_digit != 1:
    #     word_num = tens[ones_digit]                                         #tens place
    elif tens_digit and ones_digit == 0:                                    #multiples of 10
        word_num = tens[ones_digit]
    else:
        word_num = f'{tens[tens_digit]} - {ones[ones_digit]}'
    return word_num

print(converter())

#version 2


