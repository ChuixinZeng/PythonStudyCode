# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 生成器并行计算

# 生产者（生产包子）消费者（消费包子）模型

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
c = consumer("Chenronghua")
c.__next__()
b1 = "韭菜馅" # send在调用yield的同时会给yield传值
c.send(b1)
c.__next__()
'''
输出的结果：
Chenronghua 准备吃包子啦!
包子[韭菜馅]来了,被[Chenronghua]吃了!
包子[None]来了,被[Chenronghua]吃了!
'''


# 下面是边做边吃的单线程下的并行效果，三个任务同时运行
# 虽然还是串行的，但是给人感觉是并行的，效率高
print("------下面是边做边吃的并行效果--------")
def producer(name):
    c = consumer('消费者A') # 这个动作只是变成了生成器
    c2 = consumer('消费者B')
    c.__next__()  # 在这个地方next一下之后，才会打印：消费者A 准备吃包子啦!
    c2.__next__()
    print("老子开始准备做包子啦，一个包子分两半!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")
