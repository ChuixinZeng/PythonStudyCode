# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

count = 0
while True:
    print("count:",count)
    count = count+1  #相当于count+=1
    if count == 1000: # while循环1000次之后就退出
        break