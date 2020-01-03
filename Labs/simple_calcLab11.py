#lab 11 Simple Calculator
# Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.


#user inputs
# operation_in = input('What is the operation you\'d like to perform? (+, -, *, /), enter \'done\' to quit: ')

#moved these to the else in the while loop, because we don't run them unless operation_in != done ~
# user_num1 = int(input('What is the first number?: '))
# user_num2 = int(input('What is the second number?: '))


def mathematical(a,b):
            if operation_in == '+':
                added = a + b
                return added
            elif operation_in == '-':
                subracted = a - b
                return subracted
            elif operation_in == '*':
                multiply_by = a * b
                return multiply_by
            else:
                divide_by = a/b 
                return divide_by

while True:
    operation_in = input('What is the operation you\'d like to perform? (+, -, *, /), enter \'done\' to quit: ')
    if operation_in == 'done':
        print('Okay, have a nice day!')
        break
    else:
        user_num1 = int(input('What is the first number?: '))
        user_num2 = int(input('What is the second number?: '))
        print(mathematical(user_num1,user_num2))
        # break - leave out so it can loop


