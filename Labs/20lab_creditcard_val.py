


def main():
    user_card = [int(i) for i in (input('Enter your 16-digit credit card number: '))]  #this is awesome, this loops every integer in the user input str and turns it into an int (IN A LIST)

    checkdigit = user_card.pop(15)
    print(checkdigit)

    user_card.reverse()
    print(user_card)
    user_card_dubs = []
  
    for i in user_card:
        if i % 2 == 0:
            user_card_dubs.append(user_card[i]* 2)
        else:
            user_card_dubs.append(user_card[i])
    print(user_card_dubs)


    for i in range(len(user_card_dubs)):
        if user_card_dubs[i] > 9:
            user_card_dubs[i] -= 9
        else:
            continue

    sum_all = 0
    for i in user_card_dubs:
        sum_all += i

    varifier = sum_all%10
    print(sum_all)
    print(varifier)
    print(checkdigit)
    if varifier == checkdigit:
        print('Valid!')
main()

# Use this credit card number to test 4556737586899855