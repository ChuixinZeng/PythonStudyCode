# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

'''
# range(10)的结果是0-9

for i in range (10):
    print("loop",i)

# 奇偶数打印

# 每隔一个跳过一个
for i in range (0,10,2):
    print("loop",i)

# 每隔两个跳过一个
for i in range (0,10,3):
    print("loop",i)
'''

for i in range (0,10):
    if i < 3:
        print("loop",i)
    else:
        continue #通过设置断点可以看出，3以后的数字，continue是跳出本次循环，进入下次循环，而break是结束本次循环
    print("hehe...")



#循环套循环，每大循环一次，小循环执行10次

for i in range(10):
    print('----------',i)
    for j in range(10):
        print(j)
        if j > 5:
            break #只是当前结束小循环

