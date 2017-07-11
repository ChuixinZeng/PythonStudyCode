# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# os.py跟操作系统进行交互

import os

# 调用执行windows命令，只执行命令，不保存结果
os.system("dir")

# 调用的windows命令是实时执行的，不会保存到变量中，下面保存到变量中之后，只会返回命令执行成功0，失败1的标志
cmd_result = os.system("dir")
print("-->", cmd_result)

# 执行命令并保存结果,也没有中文乱码了，结果保存在内存的某个地方，通过read取出来
cmd_result = os.popen("dir").read()
print("-->",cmd_result)

# 创建一个目录
os.mkdir("new_dir")
