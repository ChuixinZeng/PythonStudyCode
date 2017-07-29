# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 除了0，其他的都为真，下面是false
print(all([0,-1,3]))

# 只要列表有一个数据为真，就返回真，列表为空，就是false
print(any([0,-1,3]))

# 把列表打印成字符串形式
print(ascii([1,3,"开挂"]))
a = ascii([1,3,"开挂"])
print(type(a)) # 列表变成字符串了

bin(1) # 十进制转换二进制，转换的是数字，不是字符串
bool(1) # 判断真假，0就是假

a = bytes("abcde",encoding="utf-8")
print(a.capitalize()) # 字符串不可以修改，这里a大写是生成了一个新的字符串
b = bytearray("abcde",encoding="utf-8") # 可修改的字符串
print(b[0]) # 把字母a对应的ASCII吗打印出来
b[1] = 100 # 修改的时候，必须以ASCII码的形式进行修改
print(b)

print(callable([])) # 判断是不是可以调用，这里[]列表返回的是false，如果是加括号()的就可以调用，比如函数
def sayhi():pass
print(callable(sayhi))

# 输入一个数字（必须是数字），返回ASCII对应的表信息
print(chr(222))

# 输入一个ASCII码的字符，返回对应的数字
# Return the Unicode code point for a one-character string.
# print(ord(11))

# compile函数用于 底层将字符串编译成可执行的代码，类似于import模块然后执行
code = '''
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
'''
py_obj = compile(code,'error.log','exec')
print(py_obj)
exec(code)

# dir可以查看对应的方法
a = {}
print(dir(a))

# 返回商数和余数
print(divmod(5,3)) # 5除以3的商数和余数

# eval只能算简单的加减乘除
x =1
print(eval('x+1'))

# filter
# 下面的方法假如在程序里面只会调用一次，就没必要单独写一个函数，所以可以写匿名函数，用完就释放了
def saaa(n):
    print(n)
saaa(3)

# lambda只能处理简单的函数，但是如果函数里面有复杂的逻辑，比如for循环，就处理不了了，可以处理三元运算
print((lambda n:print(n))(5))
calc = lambda  n:print(n)
print(calc(5))

# 三元运算，如果n <4 比如n =2,n= 1,那么n的值就是3，如果n>4，那么n的值就是赋予的值
calc = lambda  n:3 if n<4 else n
print(calc(2)) # n = 3
print(calc(5)) # n = 5

# 使用filter从一组数据里面过滤自己想要的，下面就是把大于5的都打印出来
# 这就是lambda和filter结合的使用
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)

# lambda和map结合使用
res1 = map(lambda n:n*2,range(10)) # 相当于[i*2 for i in range(10)]
for i in res1:
    print(i)

# 把所有的值累加
import functools # 在Python2里面是单独的内置函数reduce()
res2 = functools.reduce(lambda x,y:x+y,range(10))
print(res2)

# 不可变集合，类似于元组
# a = frozenset([1,4,33,22,33,444,555])

# global返回当前程序中所有变量的key:value格式
print(globals())

# hash散列
print(hash('alex')) # alex对应的hash值是不会变的，唯一的，参考图片“hash函数.png”

# 十进制转16进制
print(hex(15)) # 结果是0XF

def sample1():
    local_var = 333
    print(locals()) # 只打印local变量
sample1()
# print(globals()) # 只打印全局变量，肯定是没有local_var的
print(globals().get('local_var'))

# max min用于返回列表的最大值和最小值

# Python里面一切皆对象，列表、字符串都是对象，是对象就有属性、方法

# 转八进制,逢八进一
print(oct(8))
print(oct(9))

# 返回3的3次方
print(pow(3,3))

# round保留小数点后几位
print(round(1.3333,2))

# sorted
a = {6:2,8:0,1:4,-5:6,99:11,4:22}
print(a) # 默认打印字典是无序的
print(sorted(a)) # 对key进行排序
print(sorted(a.items())) #对key value进行排序
print(sorted(a.items(),key=lambda x:x[1])) # 按照value进行排序

# Python里面一切数据类型都是由type()函数产生的
#返回一个对象的所有属性名称用var()

# 把a和b一一对应组合起来，使用zip函数
a = [1,2,3,4]
b = ["a","b","c","d"]
for i in zip(a,b):
    print(i)

# 默认情况下可以使用import来导入模块名，如果不知道模块名的话，只知道字符串
__import__('装饰器_小高潮')