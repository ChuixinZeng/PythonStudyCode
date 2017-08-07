# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 实现用户输入用户名和密码，当用户名为 seven 或 alex 且 密码为 123 时，显示登陆成功，否则登陆失败，失败时允许重复输入三次

for i in range(3):
    username = input("username:")
    password = input("password:")
    if username == "seven" or username == "alex":
        if password == "123":
            print("success")
            break
        else:
            print("用户名或密码不对，请重新输入")
            continue
    else:
        print("用户名或密码不对，请重新输入")
        continue
else:
    print("错误超过三次，已中断")
