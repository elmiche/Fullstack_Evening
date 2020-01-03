#Practice 1

# def add(a, b):
#     return a + b
# #print(add(5, 2))
# #print(add(8, 1))

#Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

a = input('give me a number:')

user_num = int(a) 

if (user_num %2) == 0:
    print('Even')
else: 
    print('Odd')