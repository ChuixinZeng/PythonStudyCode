# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 使用while循环实现输出2-3+4-5+6...+100 的和

i,b = 2,0
while i <= 100:
    if i%2 == 0:
        b = b+i
    else:
        b = b-i
    i += 1
print(b)
