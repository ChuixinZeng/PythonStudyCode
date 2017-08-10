# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 装饰器是一种语法糖
# 模拟写网站，一个页面代表一个函数，要求其中20个页面验证后才能登陆
import time

user,passwd = "alex","abc123"
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:",*args,**kwargs)
            if auth_type == "local":
                username = input("username:").strip()
                password = input("password:").strip()

                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    # res的值来自于被装饰的函数home
                    res = func(*args, **kwargs)  # from home，默认到这个地方不会返回home里面定义的返回值from home
                    print("after authenticaiton")
                    return res # 这里才真正返回home函数的内存地址

                else:
                    exit("\033[31;1mUser has error password\033[0m")
            elif auth_type == "ldap":
                print("ldap还没实现")
        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page")

@auth(auth_type="local") # 相当于home = wrapper()
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

index()
home()
# print(home()) # 相当于调用wrapper，没有返回值，如果希望能返回home里面的返回值，就需要修改wrapper
bbs()

