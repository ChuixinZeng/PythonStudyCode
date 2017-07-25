# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 在整个程序中都生效的变量就全局变量
school = "oldboy" # 在函数中可以访问

# 函数就是变量name = alex li的作用域，这个变量只在该函数里生效
def change_name(name):
    # global school # 在函数里面改全局变量，然后函数外面的school就变成Mage Linux了
    school = "Mage Linux"
    print("before change",name,school) # 这个地方打印的school是Mage Linux，应用局部变量
    name ="alex li"
    print("after change",name)
name = "alex"
change_name(name)
print(name) # 打印的结果还是alex，因为函数里面的是局部变量，alex li只在函数里面生效
print(school) # 这个打印的结果是oldboy，全局变量定义的