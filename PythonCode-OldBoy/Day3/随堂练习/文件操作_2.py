# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

f = open('yesterday.md','r',encoding='utf-8')

# 读取前五行
for i in range (5):
    print(f.readline())

print('------------------分隔符,low循环---------------')
g = open('yesterday.md','r',encoding='utf-8')
# 将文本读取成一个列表，然后打印列表的每一行，strip是去掉\n换行空格
for line in g.readlines():
    print(line.strip())

print('------------------分隔符，low循环---------------')
# 第一种方式：把文件循环一遍，到第10行的时候不打印
# 这种是把文件先读到列表，如果文件特别大，效率就很低，所以f.readlines只适合读小文件
h = open('yesterday.md','r',encoding='utf-8')
for index,line in enumerate(h.readlines()):
    if index == 9:
        print('----------我是第10行--------------')
        continue
    print(line.strip())

print('------------------分隔符，高逼格循环---------------')
# 第二种方式：效率更高，可以变成循环一行，打印一行，然后从内存里清除一行，这样内存里只保存有一行，就可以读大文件了
j = open('yesterday.md','r',encoding='utf-8')
# 因为文件已经变成了一个叫迭代器的东西，下周学
count = 0
for line in j:
    if count == 9:
        print('----------我是第10行--------------')
        count += 1 # 如果不加这一句，则下面的continue会一直打印第十行知道循环结束
        continue
    print(line)
    count += 1
