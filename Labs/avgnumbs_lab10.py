#average numbers lab 10



#VERSION 2
#Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.


user_list = []
while True:
    user_input = input('Enter a number to add to a list, type \'done\' when complete: ')
    if user_input == 'done':
        break
    else:
        user_list.append(int(user_input))
print(f'Here is your list: {user_list}')


def add_sum(nums):
    my_sum = 0
    for num in nums:
        my_sum += num
    return my_sum   
print(f'The average is {add_sum(user_list)//len(user_list)}')

# #Version 1
# nums = [5, 0, 8, 3, 4, 1, 6]
# #adding sum
# def add_sum(nums):
#     my_sum = 0
#     for num in nums:
#         my_sum += num
#     return my_sum                        

# print(f'The average is {add_sum(nums)//len(nums)} .')



