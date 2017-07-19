# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# python虽然有垃圾回收机制可以自动关闭文件，但是如果有1000个文件呢，只要程序不结束，这些文件都处于打开状态，所以为了避免打开文件后忘记关闭
with open('yesterday4.md','r',encoding='utf-8') as f:
    for line in f:
        print(line)

# 上面的语句不需要写关闭语句，因为执行完成后，with语句就会自动关闭

# 在Python 2.7中，with语句只能打开一个文件，在Python 3.x中可以打开多个文件

with open('yesterday4.md') as obj1, open('yesterday.md') as obj2:
    pass
# 官方开发规范：一行代码不应该超过80个字符，所以代码建议按照下面的方式写

with open('yesterday.md','r',encoding='utf-8') as f1,\
        open('yesterday4.md','r',encoding='utf-8') as f2:
    for line in f1:
        print(line)
