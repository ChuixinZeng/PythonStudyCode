# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

#  商品列表是动态的，可能随时变大或变小，所以不能写字符串的形式去存，那样就写死了
# 使用嵌套列表，把价格和产品信息放到一个列表里面

product_list = [
    ('iphone', 5800),
    ('macpro', 9800),
    ('bike', 800),
    ('watch', 10600),
    ('coffee', 31),
    ('alex python', 120),
]

# 定义一个空列表，用于保存购物车
shopping_list = []
# 工资只输入一次，所以放在循环外面
salary = input("Input your salary:")
# 判断如果工资为整数
if salary.isdigit():
    salary = int(salary) # 把工资默认的字符串类型转换为int类型
    while True:
        # 通过使用enumerate来直接循环到索引号和产品名称
        for index, item in enumerate(product_list):
            print(index, item)
        '''
        for item in product_list:
            # 可以通过下标来当产品编号
            print(product_list.index(item),item)
        break
        '''
        user_choose = input("选择要买的商品>>>:") # 判断用户输入的是不是数字，是不是小于商品列表的长度
        if user_choose.isdigit():
            user_choose = int(user_choose) # 如果用户输入的是数字，则从string转换成int
            # 判断输入的编号是不是在商品编号范围内
            if user_choose < len(product_list) and user_choose >= 0:
                # 将用户选择的商品放到p_item中，通过下标把商品取出来
                p_item = product_list[user_choose]
                if p_item[1] <= salary: #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1] # 减掉购买的商品金额以后的余额
                    # \033[31;1m%s\033[0m这是加颜色
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item, salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]\033[0m" % salary)
            else:
                print("商品[%s]不存在！" % user_choose)
        elif user_choose == 'q':
            # 退出后打印已经购买的商品和余额
            print('-----------购物车商品列表------------.')
            for p in shopping_list:
                print(p)
            print("你的账户余额：",salary)
            exit()
        else:
            print("invalid option")


