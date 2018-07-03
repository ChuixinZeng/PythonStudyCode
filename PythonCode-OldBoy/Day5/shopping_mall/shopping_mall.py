# -*- Coding:utf-8 -*-

# 优化版的购物车
# 用户入口：
# 1.商品的信息存到文件里
# 2.已购商品，余额记录
# 商家入口：
# 1.可以添加商品 2.修改商品价格
# 存储商品列表
import fileinput
from core import accounts

product_list = []
f = open("D:\GitCode\PythonStudyCode\PythonCode-OldBoy\Day5\shopping_mall\\product.txt", "r")  # 打开文件
for line in f.readlines():
    line = line.strip()  # 去掉最后一个换行符
    index, item = line.split(":")  # 以冒号分割得到前后两个数据
    product_list.append((index, item))  # 添加的数据
f.close()


def print_product_list():
    for index, item in enumerate(product_list):
        print(index, item)


# 用户入口
# 用户购物
def user_shopping(account_data):
    #salary = input("请输入你的薪水：")
    salary = account_data['account_data']['balance']
    print_product_list()
    if salary > 0:
        shopping_list = []  # 存放用户购物车清单
        while True:
            option = input("喜欢那个就买哪个,按q结账退出，(对应的标号)：")
            if option.isdigit():
                option = int(option)
                if option >= 0 and option <= len(product_list):
                    p_item = product_list[option]  # 用户选择的商品
                    # print(product_list)
                    # print(p_item[1])
                    c_num = int(p_item[1])
                    if salary >= c_num:
                        shopping_list.append(p_item)
                        salary -= c_num
                        print("添加购物车成功,你的余额还有%s" % (salary))
                    else:
                        print("你的余额不足，只剩%s元" % (salary))
                else:
                    print("输入错误，请重新输入！")
            elif option == "q":
                print("----------------购物清单---------------")
                for s_list in shopping_list:
                    print(s_list)
                print("你的余额为%s" % (salary))
                account_data['account_data']['balance'] = salary
                #print(account_data)
                accounts.dump_account(account_data['account_data'])#写入文件
                print("..........exit.........")
                exit()
            else:
                print("无效的输入")
    else:
        exit("余额不足！")


# 商家入口
# 商家添加商品
def add_product():
    name_of_product = input("请输入你要添加的商品名字：")
    price_of_product = input("请输入你要添加商品的价格：")
    f = open("product.txt", "a")
    f.write(str("\n" + name_of_product) + ": %s" % (price_of_product))
    f.close()
    print("添加成功！\nexit----------")


# 修改商品价格
def change_price():
    print_product_list()  # 打印商品列表
    choice = input("请输入你的选择：")
    # name_of_change = input("请输入你要改变的商品名字")
    price_of_change = input("请输入你要改变商品的价格：")
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice <= len(product_list):
            p_item = product_list[choice]  # 选择的商品
            # c_num = int(p_item[1])#转换成int类型
            for line in fileinput.input("product.txt", inplace="%s" % (choice)):  # 对输入的选择行进行修改
                line = line.replace("%s" % (p_item[1]), "%s" % (price_of_change)).strip()
                print(line)
            exit("修改成功！")
        else:
            print("输入无效")
    else:
        if choice == "q":
            exit("退出")


def main_menu(account_data):
    print("--------------------------"
          "--------------------------"
          "\n"
          "                  欢迎进入购物菜单      "
          "\n"
          "\n"
          "商家请按b，用户请按c\n"
          "--------------------------"
          "--------------------------")
    c_num = input("请输入你的选择：")  # 使用者选择
    if c_num == "b":
        print("--------------------------"
              "--------------------------"
              "\n"
              "                  欢迎进入商家界面      "
              "\n"
              "\n"
              "添加商品请按a，修改价格请按c\n"
              "--------------------------"
              "--------------------------")
        c_num2 = input("请输入你的选择：")
        if c_num2 == "a":
            # 实现添加商品功能
            add_product()
        if c_num2 == "c":
            # 实现商品价格修改功能
            change_price()
        else:
            print("输入有误！")
    if c_num == "c":
        print("--------------------------"
              "--------------------------"
              "\n"
              "                  欢迎进入用户界面      "
              "\n"
              "\n"

              "--------------------------"
              "--------------------------")
        # 购物功能
        print(account_data)
        user_shopping(account_data)
    else:
        print("输入有误程序退出！")