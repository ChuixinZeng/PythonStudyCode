# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 读操作，只能读，如果不写r则默认就是读模式
f = open('yesterday.md','r',encoding='utf-8')  # 打开文件
first_line = f.readline() # 读取第一行
print('first_line',first_line) # 打印第一行
print('我是分割线'.center(50,'-'))
data = f.read() # 读取剩下的所有的内容，文件大时不要使用
print(data) # 打印文件

# 这种方式打开文件如果不指定编码字符集的话，默认是GBK，就会有编码问题
# 这种操作不规范，正常操作应该是先打开，然后赋予变量，在变量中修改或读取，然后再关闭文件
# data = open('yesterday','r',encoding='utf-8').read()
data = open('yesterday.md','r',encoding='utf-8').read()
print(data)

# 应该用下面这种方式
f = open('yesterday.md','r',encoding='utf-8') # 文件句柄，就是文件的内存对象，即这个文件包含什么东西
data = f.read()
data2 = f.read()
print('---------------data------------')
print(data)
print('---------------data2-----------')
# data2是空的，文件已经被data读完了
print('data2',data2)
f.close()

# 写操作，只能写，相当于重新建了一个文件，原始文件被清空了
# f.write('我爱北京天安门，天安门前太阳升')
# 当尝试往一个不存在的文件里面写东西的时候，相当于又新建了一个文件
d = open('yesterday2','w',encoding='utf-8')
# 追加写入到文件
d.write('我爱您\n')
d.write('我也爱你\n')
d.close()

# a代表追加写入，不覆盖原来的文件，但是不能读
e = open('yesterday2','a',encoding='utf-8')
e.write('我爱北京天安门\n')
e.write('woaini')
e.close()


