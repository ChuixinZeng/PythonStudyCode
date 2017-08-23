# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import conf,core
from core import login
from core import _add_user
from conf import  setting
# 自定义欢迎信息
info = '''
1. 按"A"注册
2. 按"B"登录
3. 按"Q"退出
'''

# 定义一个main函数，用于初始登录界面的判断
def main():
    # 执行while循环
    while True:
        # 打印登录提示信息，info信息定义在程序的开头，是一个字符串类型
        print(info)
        # 提供交互式界面，让用户输入指令信息
        command = input('请输入指令：').strip()
        # 如果用户输入的是大写的A，则调用_add_user函数，创建新用户
        if command.upper() == 'A':
            core._add_user._add_user()
        # 如果用户输入的是大写的B，则调用_login函数，进行登录
        elif command.upper() == 'B':
            core.login._login()
        # 如果用户输入的是Q，则调用_logout函数，退出登录
        elif command.upper() == 'Q':
            core.login._logout()
        # 如果用户没有按照提示信息进行输入，则告诉用户重新输入，会重新执行while循环
        else:
            print('输入错误，请重新输入')

# 执行main函数
if __name__ == '__main__':
    main()
setting.setlog()
