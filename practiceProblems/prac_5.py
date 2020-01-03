#practice 5
#Print out the powers of 2 from 2^0 to 2^20


def powersOf2():
    power = 0
    while power <= 19:
        power += 1
        equation = 2 ** power
        print(equation)
      


powersOf2()