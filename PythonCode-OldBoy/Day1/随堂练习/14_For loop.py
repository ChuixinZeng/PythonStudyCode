# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

for i in range(10):
    if i>5:
        continue #不往下走了,直接进入下一次loop，前五次循环到continue就结束了，不会往下走继续打印print
    print("loop:", i )

# 打印结果是：
# loop: 5
# loop: 6
# loop: 7
# loop: 8
# loop: 9