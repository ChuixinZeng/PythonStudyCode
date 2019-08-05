# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 实现用户输入用户名和密码，当用户名为 seven 且 密码为 123 时，显示登陆成功，否则登陆失败!
username = input("pls input username:")
password = input("pls input password:")
while True:
    if username == "seven" and password == "123":
        print("登录成功")
        break
    else:
        print("请输入正确的用户名和密码")
        continue
