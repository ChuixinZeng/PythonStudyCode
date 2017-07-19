# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import sys,time

for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush() # 必须加这一句，不然看不到实际的刷新效果，数据是一次性输出的
    time.sleep(0.1)