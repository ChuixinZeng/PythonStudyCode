# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 斐波拉契数列

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print(b) # 通过a计算出b的值，打印出来就是斐波拉契数列
        a,b = b,a+b
        # 公式分解
        # 相当于元组t = (b,a+b) a=t[0] b= t[1]，当b=1的时候，a=b，即a=1；当a=1的时候，b=a+b=1+1=2，即a=1，b等于2
        # 当b=2的时候，a=b，即a=2；当a=2的时候，b=a+b=1+2=3，即a=2，b等于3
        n = n +1
    return 'done'

fib(10) # 从1开始生成10个斐波拉契数列


# 用函数做生成器，直接把print改成yield就是生成器了
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        # 公式分解
        # 相当于元组t = (b,a+b) a=t[0] b= t[1]，当b=1的时候，a=b，即a=1；当a=1的时候，b=a+b=1+1=2，即a=1，b等于2
        # 当b=2的时候，a=b，即a=2；当a=2的时候，b=a+b=1+2=3，即a=2，b等于3
        n = n +1
    return 'done'

print(fib(10)) # 变成生成器了，一个内存地址
f = fib(10)
print(f.__next__())
print("干点别的事情") # 生成器的好处是可以随时进出程序，前面进去程序循环一次之后，出来做个事情，然后后面可以继续进入循环
# 通过使用生成器可以实现单线程的并行计算的效果，而不是等待fib全部执行完后的串行效果
print(f.__next__())
print(f.__next__())

print("start loop")
# 用for循环，前面的done就不会打印了，如果不用for直接next，取到取不出来的时候，就会抛出异常
for i in f:
    print(i)


# 异常处理，一直到next出错的的时候，就会执行except里面的代码
# return在生成器里面的作用
# 只要fib函数里面包含yield，就不是单纯的函数了，而是生成器

g = fib(10)
# 函数里面每执行一次，就中断一次，回到外面执行下面的循环，然后再回到函数执行，再中断
# 所以yield是返回当前函数的中断状态的值，想什么时候回来就什么时候回来
while True:
    try:
        x = next(g)
        print("g:",x)
    except StopIteration as e:
        print("Generatior return value:", e.value)
        # 执行结果是Generatior return value: done，这个done是在函数里面的return定义的
        break
