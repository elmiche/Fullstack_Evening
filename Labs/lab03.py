#lab03.py
#Grading

#version 1
user_score = input("Find out your letter grade, enter your score:")
user_grade = int(user_score)

#this is the code that converts numeric ranges to symbolic letters
# if user_grade >= 90 and user_grade <=100:
#     print("A")
# elif user_grade >= 80 and user_grade <=89:
#     print("B")
# elif user_grade >= 70 and user_grade <=79:
#     print("C")
# elif user_grade >= 60 and user_grade <=69:
#     print("D")
# elif user_grade >= 0 and user_grade <=59:
#     print("F")
# else: done


#version2
if user_grade >= 96 and user_grade <=100:
    print("A+")
elif user_grade == 95:
    print("A")
elif user_grade >= 90 and user_grade <=94:
    print("A-")
elif user_grade >= 86 and user_grade <=89:
    print("B+")
elif user_grade == 85:
    print("B")
elif user_grade >= 80 and user_grade <=84:
    print("B-")
elif user_grade >= 76 and user_grade <=79:
    print("C+")
elif user_grade == 75:
    print("C")
elif user_grade >= 70 and user_grade <=74:
    print("C-")
elif user_grade >= 66 and user_grade <=69:
    print("D+")
elif user_grade == 65:
    print("D")
elif user_grade >= 60 and user_grade <=64:
    print("D-")
elif user_grade >= 0 and user_grade <=59:
    print("F")

else: done



#version3
