# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 将 name 变量对应的值中的 “l” 替换为 “p”，并输出结果

#第一种
name = " aleX"
name = name[:2]+"p"+name[-2:]
print("name:",name)

#第二种
name = " aleX"
name1 = ""
for i in name:
    i = "p" if i == "l" else i #三元运算
    name1 += i
print("name1:",name1)

#第三种
name = " aleX"
name1 = ""
for i in name:
    if i == "l":
        i = "p"
    name1 += i
print("name3:",name1)