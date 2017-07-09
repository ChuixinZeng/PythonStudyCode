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
    count += 1

    #设置计数器是否重新开始

    if count == 3:
        continue_confirm = input("do you want to keep guessing?")
        if continue_confirm != 'n': #不等于n就继续，等于n就退出
            count = 0

#else:
    #print("you have tried too many time...fuck off")