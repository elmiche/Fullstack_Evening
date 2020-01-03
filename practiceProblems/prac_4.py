#Practice problem 4
#Write a function that returns the maximum of 3 parameters.

def max_int(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c: 
        return b
    if c > b and c > a:
        return c 

print(max_int(1,2,3))