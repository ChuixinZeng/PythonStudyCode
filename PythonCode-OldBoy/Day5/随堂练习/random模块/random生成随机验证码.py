# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import random
# checkcode用于保存最终要生成的字符串类型的数据，就是保存验证码的
checkcode = ''
# 设置验证码长度为4位
for i in range(4):
    # 0,1,2,3
    current = random.randrange(0,4)
    # 猜测的值的结果，如果current随机的值不等于i的值，则temp当前loop的值为字母
    if current != i:
        # chr用于ASCII码转换为字母
        # 65-90是大写字母从A到Z
        temp = chr(random.randint(65,90))
    # 如果current等于i的话，则随机生成数字
    else:
        temp = random.randint(0,9)
    # 把temp转换成字符串类型，然后传给checkcode
    checkcode += str(temp)
print (checkcode)