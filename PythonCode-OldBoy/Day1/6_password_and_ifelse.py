# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
#下面的密文密码如果想看到执行的效果，需要到Day1目录下面使用Python命令行看效果
import getpass

#不加''代表是变量

_username = 'zengchuixin'
_password = 'abc123'
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")
print(username,password)

#下面的print有缩进，跟其他语言的{}是一个意思，只要出现indentationerror就代表是缩进错误

if _username == username and _password == password:
    print("welcom user {name} login...".format(name=username))
else:
    print("Invalid username or password!")