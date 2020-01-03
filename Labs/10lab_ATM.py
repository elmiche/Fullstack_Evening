#lab 10

# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0. Implement the initializer, as well as the following functions:

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it



class Atm_machine:

    def __init__(self):
        self.total_bal = 0
        self.transaction_tracker = []
    
    def check_balance(self):
        return self.total_bal
    
    def deposit(self, amount):
        self.total_bal += amount
        self.transaction_tracker.append(f'Added ${amount}, total is {self.total_bal}')    
        return self.total_bal

    def check_withdrawal(self, amount):
        if self.total_bal - amount >= 0:
            return self.total_bal
        else:
            return 'overdrawn'
    
    def withdraw(self, amount):
        self.total_bal -= amount #subtract amount
        self.transaction_tracker.append(f'withdrew ${amount}, total is {self.total_bal}') 
        return self.total_bal
    
    def print_transactions(self):
        print(self.transaction_tracker)



#instantiation
bbsfirst_ATM = Atm_machine()

while True:
    user_action = input('What would you like to do? (deposit, withdraw, check balance, history)?: ')     
    
    if user_action == 'deposit':    
        bbsfirst_ATM.deposit(int(input('How much money you got?: ')))
        print(f'total balance is {bbsfirst_ATM.check_balance()}')
    elif user_action == 'check balance':
        print(f'total balance is {bbsfirst_ATM.check_balance()}') 
    elif user_action == 'withdraw':
        amount = int(input('How much would you like to withdraw?: '))
        if bbsfirst_ATM.check_withdrawal(amount) == 'overdrawn':
            print('overdrawn')
        else:
            print(bbsfirst_ATM.withdraw(amount))
    elif user_action == 'history':
        print(bbsfirst_ATM.print_transactions())
    else:
         print('not a valid entry') 





