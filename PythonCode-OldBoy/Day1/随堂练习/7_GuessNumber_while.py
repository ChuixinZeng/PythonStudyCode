# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
age_of_oldboy = 56

#计数器从循环外面开始
count = 0
while  count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!")

    #计数器结束
    count +=1
else:
    print("you have tried too many time...fuck off")