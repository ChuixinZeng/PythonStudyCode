# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

from core import login
from core import _top_up
from core import _load_database
from core import _get_shopping_history
from core import _get_balance
from core import _set_balance
from core import _set_shopping_time
from core import _set_shopping_list

# 自定义错误提示信息
_error_info = '输入有误，请检查后重新输入！'

# 定义一个函数_shopping，用于执行购物程序
def _shopping(account):
    # 定义一个字典，用于保存商品菜单
    goods = {'家电类': {'电视': {'小米电视': 3999, '乐视电视': 4299},
                     '空调': {'格力空调': 8999, '海尔空调': 6000},
                     '冰箱': {'美的冰箱': 5099, '西门子冰箱': 4599}},
             '3C类': {'电脑': {'联想笔记本': 6888, 'mac air': 8009},
                     '手机': {'小米5': 1999, 'iPhone6': 5299}},
             '生活类': {'鞋子': {'NIKE篮球鞋': 899, '安踏': 399},
                     'T恤': {'森马': 89, '真维斯': 75, '优衣库': 97}}}
    # 第一级死循环
    while True:
        # 通过使用enumerate来直接循环到产品名称
        for i in enumerate(goods.keys()):
            # 打印第一级菜单
            print(i)
        # 提供交互式界面，让用户输入要选择的商品分类名称，选择一级菜单
        choose = input('请输入您要选择的商品分类名称（输入q退出）：').strip()
        # 定义一个空字符串，用于保存二级菜单
        str1 = ''
        if choose in goods:
            # 如果用户输入的商品分类正确，则将该商品分类下的所有商品打印出来
            for i in enumerate(goods[choose].keys()):
                # 打印用户选择的一级菜单下面的二级菜单
                print(i)
                # 将二级菜单追加添加到str1变量中
                str1 += (i[1] + '\n')
            # 所有二级菜单均添加到str1之后，在str1后面加上：
            str1 += ':'
            # 第二级死循环
            while True:
                # 分类来自于前面choose的交互式输入，分类下面的列表来至于str1变量
                # 让用户选择一个二级菜单
                c_name = input("请输入您要选择的%s分类名称(输入b返回,输入q退出):\n%s"% (choose, str1)).strip()
                # 定义一个空字符串，用于保存三级菜单
                str2 = ''
                if c_name == 'b':
                    # 如果用户输入的是b，则中断当前的while循环，返回上上层循环，即返回到上层菜单
                    break
                elif c_name == 'q':
                    # 如果用户输入的是q，则调用_log_out函数，退出登录
                    login._logout(account)
                # 如果用户输入的名称在二级菜单里面，则通过for把用户选择的二级菜单商品下面的三级菜单遍历出来
                elif c_name in goods[choose]:
                    for i in goods[choose][c_name].keys():
                        # 打印遍历出来的二级菜单下面的三级菜单，同时打印物品和价格
                        # i来自于keys即键名称（物品名称），goods[choose][c_name][i]取的是键的值，即价格
                        print(i,goods[choose][c_name][i])
                        str2 += (i + '\n')
                    str2 += ':'
                    # 第三级死循环
                    while True:
                        # 在交互式界面，让用户输入要购买的商品的名称，商品目录来自于str2变量
                        p_name = input('请输入您要购买的商品名称（输入b返回上一级，q退出，h查询购物车）:\n%s'
                                       % str2).strip()
                        # 如果用户输入的是b，则跳出本层级的while死循环，退到上一级
                        if p_name == 'b':
                            break
                        # 如果用户输入的q，则直接调用_logout函数，退出购物
                        elif p_name == 'q':
                            login._logout(account)
                        # 如果用户输入的h，则查询json文件中的购物历史
                        elif p_name == 'h':
                            database = _load_database._load_database()
                            # 有购物历史，则调用_get_shopping_history函数，输出购物历史
                            if database[account]['shopping_time'] != None:
                                _get_shopping_history._get_shopping_history(account)
                            # 梅花购物历史的话，则告诉用户无购物历史
                            else:
                                print('您在本商城没有购物记录！')
                        # 如果用户输入的商品名称在所选择的商品分类中
                        elif p_name in goods[choose][c_name]:
                            # 第四层死循环
                            while True:
                                # 交互式界面让用户输入要购买的商品的数量
                                num = input('请输入要购买的商品的数量:').strip()
                                # 如果用户输入的是纯数字
                                if num.isdigit():
                                    # 首先将纯数字转换为整型
                                    num = int(num)
                                    # 定义一个account_balance变量，保存现在的账户余额
                                    account_balance = _get_balance._get_balance(account)
                                    # 定义一个价格变量，总价格 = 商品单价*数量，单价来自于字典，数量来自于num
                                    price = (goods[choose][c_name][p_name]) * num
                                    # 判断如果账户余额大于所购买的商品金额，才可以购买
                                    if account_balance >= price:
                                        # 调用_set_balance函数，计算购买后的账户余额是多少
                                        # #计算方法在_set_balance函数里面
                                        _set_balance._set_balance(account,price)
                                        # 提示用户已经成功购买商品
                                        print('您成功购买%d件商品:%s!'% (num,p_name))
                                        # 调用_set_shopping_list函数，将购买的商品列表保存到json文件中
                                        _set_shopping_list._set_shopping_list(account,p_name,num)
                                        # 定义account_balance变量，通过使用_get_balance函数重新获取账户的余额信息
                                        account_balance = _get_balance._get_balance(account)
                                        # 打印告诉用户，购买完商品之后剩下多少钱
                                        print('您目前的账户余额为\033[31m%d\033[0m元' % account_balance)
                                        # 调用_set_shopping_time函数，将购物时间写入到json文件
                                        _set_shopping_time._set_shopping_time(account)
                                        # 退出当前的循环，到上一级循环，用户可以选择是否继续购物
                                        break
                                    # 如果用户的账户余额小于商品的金额，则告诉用户余额不足，无法购买
                                    else:
                                        print('您的账户余额不足，请您及时充值！')
                                        g = input("充值输入t，返回上一级输入b，退出输入q':")
                                        if g == 'q':
                                            login._logout()
                                        if g == 'b':
                                            break
                                        if g == 't':
                                        # 这里我增加了一个调用_top_up函数，账户余额不住的时候，马上提示用户充值
                                            _top_up._top_up(account)
                                # 如果用户购买商品时输入的数量不是纯数字类型，则调用_error_info函数，输出错误信息
                                else:
                                    print(_error_info)
                        # 如果用户输入的购买的商品名称不正确，则调用_error_info函数，输出错误信息
                        else:
                            print(_error_info)
                # # 如果用户输入的购买的商品分类信息不正确，则调用_error_info函数，输出错误信息
                else:
                    print('输入错误，请重新输入！')
        # 如果用户输入的不是商品分类，而是q，则调用_logout函数退出登录
        elif choose == 'q':
            login._logout(account)
        # 如果用户输入的信息既不在商品分类中，也不是q，则告诉用户重新输入
        else:
            print('输入错误，请重新输入！')
