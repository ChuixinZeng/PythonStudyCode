# -*- coding:utf-8 -*-

# Author:Chuixin Zeng
# 功能要求:
#
# 要求用户输入总资产，例如:2000显示商品列表，让用户根据序号选择商品，加入购物车 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
#
# goods = [ {"name": "电脑", "price": 1999},
#
# {"name": "鼠标", "price": 10},
#
# {"name": "游艇", "price": 20},
#
# {"name": "美女", "price": 998},
#
# ]
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
my_money = int(input("请输入金额："))
while True:#用于循环购买
    for i,good in enumerate(goods,1):#循环商品信息
        print(i,goods[i-1]["name"],goods[i-1]["price"])#打印列表
    user_c = int(input("请选择商品："))#输入商品序号
    if user_c >0 and user_c <=len(goods):#判断输入是否在列表中
        if int(goods[user_c-1]["price"]) <= my_money:#余额大于商品金额
            my_money = my_money - int(goods\
                                    [user_c-1]["price"])#减商品金额
            print("购买 %s 成功,余额为 %s"%(goods[user_c-1]["name"]\
                                            ,my_money))#打印成功信息
        else:
            print("余额不足!再见！")
            break
    else:
        print("无此商品！")
        continue
