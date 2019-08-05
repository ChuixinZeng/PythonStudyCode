# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 使用 while 循环实现输出 1-100 内的所有偶数

i = 1
while i < 101:
    if i%2 == 0:#取2得余数为0为偶数
        print(i)
    else:
        pass#啥也不做
    i += 1