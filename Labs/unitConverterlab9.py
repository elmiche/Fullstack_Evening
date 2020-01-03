#lab 9 Unit Converter

#TODO add comments to understand what the heck I actually did here?? 


user_distance = float(input('First, what is the distance? '))
starting_units = input('now, what are the starting units (feet, miles, km, yards, inches)? ')
final_unit = input('Lastly, what is the unit we are converting to (feet, miles, km, yards, inches)? ') 

#VERSION4 >>

def meter_magic(user_distance, starting_units):
    while True: 
        if starting_units == 'feet': 
            meters = user_distance * 0.3048
            print(f'{user_distance} {starting_units} is {user_distance * 0.3048} meters')
        elif starting_units == 'miles':
            meters = user_distance * 1609.34
            print(f'{user_distance} {starting_units} is {user_distance * 1609.34} meters')
        elif starting_units == 'km':
            meters = user_distance * 1000
            print(f'{user_distance} {starting_units} is {user_distance * 1000 } meters')
        elif starting_units == 'yards':
            meters = user_distance * 0.9144
            print(f'{user_distance}{starting_units} is {user_distance * 0.9144} meters')
        elif starting_units == 'inches':
            meters = user_distance * 0.0254
            print(f'{user_distance}{starting_units} is {user_distance * 0.0254} meters')
        else:
            print('We don\'t accept that kind of unit')
        return meters

from_meters = meter_magic(user_distance, starting_units)
#this variable is ^ calling meter_magic with parameters starting distance and starting_units
def converter_func(from_meters, final_unit):
    meters = from_meters
    if final_unit == 'feet':
        print(f'which is {meters / 0.3048} feet')
    elif final_unit == 'miles':
        print(f'which is {meters / 1609.34} miles')
    elif final_unit == 'km':
        print(f'which is {meters / 1000} km')
    elif final_unit == 'yards':
        print(f'which is {meters / 0.9144} yards')
    else:
        print(f'which is {meters / 0.0254} inches')  #inches

converter_func(from_meters, final_unit)

 
#Version4 is COMPLETE OH YEAH BABY!!!

