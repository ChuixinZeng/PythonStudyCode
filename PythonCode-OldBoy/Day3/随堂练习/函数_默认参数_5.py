# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 提前给形参赋予了一个值，就是默认参数
def test(x,y=2):
    print(x)
    print(y)
# 如果不赋值，那么y默认的值就是2
test(1)

# 赋值的话，y的值就是赋予的值
test(1,2)

# 默认参数特点：调用函数的时候，默认参数非必须传递

# 应用场合：1、默认安装值，在函数里面指定如果为ture的话就默认安装；2、指定默认端口，例如连接数据库
def conn(host,port=1433):
    pass
conn()