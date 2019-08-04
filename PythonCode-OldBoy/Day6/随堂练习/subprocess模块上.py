# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

'''
# 用Python脚本去调操作系统的命令
# 下方输出结果中文乱码，只需要把pycharm改为GBK字符集就可以了
import os
result = os.system("dir") # 输出命令结果到屏幕，返回命令执行状态
print(result) # 输出的是返回值（在Python命令行下面）
# 返回成功是0，返回不成功不一定是1，是非零

# 如果想获取dir的输出信息，就不能用os模块了，需要使用
os.popen("dir") # 在Python命令行里面返回的是内存对象
os.popen("dir").read() # 从内存对象中把结果取出来，格式是乱的
a = os.popen("dir").read()
print(a) # 格式是好的、把内存中的数据以/n进行格式化

在Python 2.7里面有一个commands模块（在Linux上比较好，Windows输出会有问题）,在3.x版本里没有了

import commands
res = commands.getstatusoutput("df")
print(res)
# 上面的方法无法判断命令的返回状态是成功还是失败
'''
# subprocess模块为了替换掉os.system os.spawn* commands
# 使用run方法去调用subprocess模块

import subprocess
# 在Linux下面，如果涉及到管道过滤，需要把整个命令放到字符串中
# shell = true意识是命令通过shell去处理，不通过Python解析了
subprocess.run('df -h | grep sda1', shell=True)
subprocess.run("[cd]")



