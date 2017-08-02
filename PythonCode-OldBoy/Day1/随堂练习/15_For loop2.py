# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

for i in range(10):
    if i>5:
        break # 打印前六次结果，然后就中断不往下走了,直接跳出整个loop
    print("loop:", i )

# 结果
# loop: 0
# loop: 1
# loop: 2
# loop: 3
# loop: 4
# loop: 5