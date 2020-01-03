# Lab 8 Make Change

#Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.



quarters = 25
dimes = 10
nickels = 5
pennies = 1


total = int(input('How many pennies do you have?: '))

#Quarters
nquarters = total // quarters
total =  total - nquarters * 25

#Dimes
ndimes = total // dimes
total =  total - ndimes * 10

#Nickels
nNickels = total // nickels
total = total - nNickels * 5

#Pennies
nPennies = total // pennies
total = total - nNickels * 1

print(f'You have {nquarters} quarters, {ndimes} dimes, {nNickels} nickels, and {nPennies} pennies!')


