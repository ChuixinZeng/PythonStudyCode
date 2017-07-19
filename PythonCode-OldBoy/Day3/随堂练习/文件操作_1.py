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

# 为什么读完的默认就不能从头读取了，因为读到哪，文件指针就在那，然后下一次从文件指针所在的位置继续读取
h = open('yesterday.md', 'r', encoding='utf-8')
print(h.tell()) # 没有读之前文件指针在0的位置
print(h.readline())
print(h.tell()) # 读取完一行之后，文件指针跑到了行尾，即72
print(h.read(5)) # 只读取前5个字符
print(h.tell()) # 文件指针又往前了5个字符
# 怎么把文件指针光标移回去
h.seek(0)
print(h.readline()) # 再打印，又回到第一行了

print(h.encoding) # 打印当前文件所使用的编码格式
print(h.name) # 打印文件的名字

# 并不是所有的文件都可以移动光标回去，例如tty文件，终端文件是不可以的
print(h.seekable()) # 判断文件指针是不是可以移动
print(h.readable()) # 判断文件是否可读
print(h.writable()) # 判断文件是否可写

#u = open('yesterday.md', 'a', encoding='utf-8')
#print(u.truncate(10)) # 从文件开头进行文件截断，不指定位置的话就是清空

j = open("yesterday3",'w')
j.write('hello\n') # 先写一行数据，目前数据还没有到文件中
print(j.flush()) # 数据实时刷新存到硬盘，比如存钱的操作，上面的数据已经刷新到了文件中
j.write('hello1\n') # 再写一行，此刻数据还没有到硬盘中
print(j.flush()) # 刷新后，数据已经到了硬盘中

# 上面是读、写、追加操作
# 打开源文件进行修改的话，默认所修改的位置会被覆盖掉，机制就是这样子的
# 读写操作，先读，后写，写的东西会追加到文件结尾
# 读写模式有点用，可以打开文件，然后追加写入
k = open('yesterday3','r+',encoding='utf-8')
print(k.readlines())
print(k.readlines())
print(k.readlines())
print(k.write('测试读写的写'))

# 写读操作，先写，后读，写的东西同样会追加到文件结尾，这个操作没什么用
# k = open('yesterday3','w+',encoding='utf-8')

# 追加读写
# k = open('yesterday3','a+',encoding='utf-8')

k = open('yesterday3','rb') # 以二进制格式读取文件，例如视频文件
print(k.readlines())
print(k.readlines())
print(k.readlines())

# 后面学的网络传输必须使用二进制文件格式
# 这里说的二进制是指以二进制格式进行编码的，而不是显示的01010，但内部是使用二进制处理的
# 二进制文件写入
k =open('yesterday3','wb')
k.write('hello binary\n'.encode())
k.close()