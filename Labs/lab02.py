#lab02.py
#Mad Libs

#version 1
# "A (animal) in the (body part), is worth (number) in the (noun)"
# madlib_animal = input("Name an animal: ")
# madlib_body = input("A Body part: ")
# madlib_numb = input("Give me a number: ")
# madlib_noun = input("Give me a noun: ")
# print(f"A {madlib_animal} in the {madlib_body}, is worth {madlib_numb} in the {madlib_noun}.")

#lol amirite
#made some changes

#Version 2

user_animals = input("Name 3 animals, separated by commas: ")
animals = user_animals.split()
user_body = input("Name 3 parts of the body, separated by commas: ")
body_parts = user_body.split()
user_num = input("Type three numbers, separated by commas: ")
number_list = user_num.split()
user_object= input("Lastly, type three random objects, separated by commas: ")
object = user_object.split()
import random

print(f"A {random.choice(animals)} in the {random.choice(body_parts)} is worth {random.choice(number_list)} in the {random.choice(object)}.")
#lorem 
