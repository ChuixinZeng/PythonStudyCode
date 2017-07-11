# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import getpass

_username = "zengchuixin"
_password = "123"

user = input("pls input username:")
pwd = input("pls input password:")

if user == _username and pwd == _password:
    print("welcom user %s login" % user)
else:
    print("wrong username or password!")

print(user,pwd)

# 如果这是一个自定义的模块，就可以在其他地方通过import方式调用这个模块
# 调用方法是在新的py文件里输入import login_custommodule.py，自定义模块和当前的py是在同一个目录
# 不在同一个目录就不执行成功，可以把自定义模块放到C:\\Program Files\\Python36\\lib\\site-packages里面，因为环境变量会找这个路径
# 还有一种方法，我们可以在环境变量里面加个自定义路径，把自定义模块所在路径放到环境变量

