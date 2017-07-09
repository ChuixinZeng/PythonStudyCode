# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

age_of_oldboy = 56

for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!")

else:
    print("you have tried too many time...fuck off")