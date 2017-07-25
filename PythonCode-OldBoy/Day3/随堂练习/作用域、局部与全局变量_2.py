# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 下面直接在函数里面强制声明一个全局变量，也是可以的
# 但是不要这么干，global不建议用，下面的用了就可能被开除，呵呵
# 原因这么干了之后，函数会在程序的很多地方调用，很难找到哪个地方调用了global，很难调试，无法调试，程序就乱了
# 切记：不要在函数里面改全局变量，如果非要改的话，就按照《作用域、局部与去全局变量_1》里面的用，里外都有定义

'''
def change_name():
    global name
    name = "alex"

change_name()
print(name)
'''

school = "Old edu."
names = ["alex","jack","rain"]
def change_name():

    names[0] = "金角大王" # 这一条修改生效的
    # 原因是只有字符串和整数是不能在局部变量里面改全局
    # 而列表、字典这种是可以直接在局部改全局的
    print('inside function',names)

change_name()
print('outside funciton',names)