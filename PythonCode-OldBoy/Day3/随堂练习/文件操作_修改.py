# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 第一种使用vim编辑器打开，文件会先读取到内存，然后在内存中修改
# 第二种方式打开一个文件，修改完了之后，写到一个新文件里面
# 在Linux shell里面可以使用sed替换

f = open('yesterday4.md','r',encoding='utf-8')
f_new = open('yesterday4.bak','w',encoding='utf-8')

for line in f:
    if "肆意的快乐" in line:
        line = line.replace("肆意的快乐","肆意的快乐等Alex享受")
    f_new.write(line)
f.close()
f_new.close()


