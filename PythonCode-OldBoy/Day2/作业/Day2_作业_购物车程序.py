# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 导入JSON模块
import json
# 导入日期时间模块
import datetime
# 导入系统OS模块
import os

# 自定义欢迎信息
info = '''
1. 按"A"注册
2. 按"B"登录
3. 按"Q"退出
'''
# 自定义错误提示信息
_error_info = '输入有误，请检查后重新输入！'

# 定义一个_save_account函数
# 用于将购物相关信息保存到JSON文件，比如购物时间，购物历史，购物列表，账户余额，创建的新用户和现有已存在用户信息
def _save_account(database, filename='DataBase.json'):
    # 打开并可写文件,若文件已存在，则以前的内容将被清除
    # 使用with as语句的效率更高，不需要单独设置如何读文件之后再如何关闭文件，一个with as搞定所有读写关闭操作
    with open(filename,'w') as f: # f相当于一个变量，把打开并修改文件的操作赋予f
        json.dump(database,f) # json.dump是将一个Python数据类型列表进行json格式的编码解析

# 定义一个_load_database函数，用于从json文件中读取信息，默认加载的数据库是database.json文件
def _load_database(filename='DataBase.json'):
    with open(filename) as f:
        database = json.load(f) # 解码JSON数据，将一个JSON编码的字符串转换回一个Python数据结构
    return database # 返回解码后的数据

# 定义一个函数_set_shopping_time,设置并记录购物的时间，函数里面定义了一个参数account，用于保存账户信息
def _set_shopping_time(account):
    database = _load_database() # 设定要记录到哪个数据库，这里使用的是前面定义好的函数_load_database定义的database.json
    d1 = datetime.datetime.now() # 设置购物时间为当前时间
    d2 = d1.strftime('%Y-%m-%d %H:%M:%S') # 将当前时间进行格式转换
    database[account]['shopping_time'] = d2 # 将转换好的时间记录到字典里面的shopping_time键上
    _save_account(database) # 保存购物时间到数据库中，这里的数据库是指database.json文件

# 定义一个函数，用于获取已经保存过的购物时间
def _get_datetime(account):
    database = _load_database()
    data = database[account]['shopping_time']
    # 返回变量data的值，变量data保存的就是account键对应的购物时间值，这个值是从json里面解码出来后到字典里
    # 由json到Python可识别的字典数据的解码过程由_load_database函数完成
    return data

# 定义一个函数_get_shopping_history，用于查询购物历史记录
def _get_shopping_history(account):
    database = _load_database()
    history = database[account]['shopping_list']
    # 增加一个空列表,配合下边for循环将购物清单中的重复项合并
    aa = []
    for i in history:
        # 将购物车里面的shopping list和aa空列表进行对比，如果列表里面没有，就添加到列表
        # 也就意味着，如果列表已经有了就不添加了，达到了购物车去重的功能
        if i not in aa:
            aa.append(i)
    # 然后循环遍历aa列表里面的购物清单
    for j in aa:
        # 统计购买的每件商品的数量，也就是aa列表里面每件商品的数量，数量从history原始列表里面取（未去重的列表）
        count = history.count(j)
        # 统计购买商品的日期，日期就是account字典对应的商品的日期
        date = _get_datetime(account)
        # 打印购买的商品的数量、日期和商品名称
        print('您于%s购买了%s件%s' %(date,count,j))

# 定义一个函数login，用于登录系统
def _login():
    database = _load_database() # 加载数据库，使用的是前面定义好的加载数据库的函数
    blacklist = _load_database('BlackList.json') # 设置用户的黑名单列表，在列表中的用户将不允许登录到购物系统
    print('欢迎登录购物系统！') # 打印欢迎信息
    # 第一个死循环
    while True:
        account = input("请输入您的账号登录系统（按q退出）：")
        if account in blacklist:
            # 如果账户在黑名单里面，则退出登录
            print("您的账号已经被锁定，请联系管理员处理！")
            _logout() # 直接调用下面定义好的_logout()函数
        # 判断如果用户输入的是q，就退出购物系统
        elif account == 'q':
            _logout()
        # 判断如果用户在数据库里面，则继续判断用户输入的密码是否正确
        # 这里使用while循环和count计数器，如果输入错误密码大于3次，则锁定账户
        elif account in database:
            count = 0
            while count < 3:
                pwd = input('请输入密码：')
                # 如果用户输入的密码和数据库保存的密码匹配
                if pwd == database[account]['pwd']:
                    # 进入到死循环
                    while True:
                        # 首先登录成功后，先获取用户账户的余额，告诉用户还剩多少钱，余额通过_get_balance函数得到
                        account_balance = _get_balance(account)
                        # 高亮打印账户的余额信息
                        print('您的账户余额是\033[32m%d\033[0m'% account_balance)
                        # 让用户输入特定字母进入特定的菜单，并使用strip去除提示信息前后的空格
                        command = input('按h查询购物历史,按s开始购物,按t充值,开始购物后购物历史将被清空:').strip()
                        # 导入用户购物信息数据库
                        database = _load_database()
                        # 判断如果用户输入的是h，则查询购物历史
                        if command == 'h':
                            # 判断如果购物时间不为空的话，证明用户有购买历史
                            if database[account]['shopping_time'] != None:
                                # 加载函数_get_shopping_history，输出购物历史信息
                                _get_shopping_history(account)
                            else:
                                print('您在本商城没有购买过东西！')
                        elif command == 't':
                            # 如果用户输入的是t，则加载定义好的_top_up函数，执行充值操作
                            _top_up(account)
                        elif command == 's':
                            # 如果用户输入的是s，则将字典中的购物列表和时间初始化为空
                            # 注意：这个字典是从json文件转换过来的，里面有历史数据，所以需要先清空
                            # 等用户购物完成后，新的字典数据，即购物数据，会写回到json文件
                            database[account]['shopping_list'] = []
                            database[account]['shopping_time'] = None
                            # 调用_save_account函数，将清空的操作保存到database文件
                            _save_account(database)
                            # 调用shopping函数，开始购物
                            _shopping(account)
                        else:
                            # 如果用户的操作不符合上面所有的情况，则输出错误信息
                            # 这里直接调用前面定义好的_error_info函数，输出错误信息
                            print(_error_info)
                else:
                    count += 1
                    # 告诉用户还有多少次机会尝试登陆
                    print('输入的密码错误，你还有%s机会' % (3 - count))
            # 将用户账号添加至blacklist,保存成字典形式,value设置为None
            # 这里使用了字典的setdefalut用法，如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值
            blacklist.setdefault(account)
            # 用户输入三次错误操作之后，会跳出上面的while循环，然后打印信息告诉用户账号已锁定
            print('您的账号已经锁定！')
            # 将锁定的账户信息保存到黑名单列表
            _save_account(blacklist,'BlackList.json')
            # 调用退出登录的函数
            _logout()
        else:
            print('账号不存在，请重试！或输入b返回上一层，输入q，退出购物程序！')

# 定义一个函数_set_shopping_list，用于设定购物清单
def _set_shopping_list(account,c_name,num):
    database = _load_database()
    # 使用for循环添加购买的商品的数量
    for i in range(num):
        # 将购买的商品添加到字典shopping_list键所对应的列表中
        database[account]['shopping_list'].append(c_name)
        # 将购买信息通过调用_save_account函数保存到json文件中
        _save_account(database)

# 定义一个函数_set_balance，用于计算购买商品后，所剩下的余额
def _set_balance(account,num):
    database = _load_database()
    # 购买商品后，扣除购买的商品的价格
    database[account]['balance'] -= num
    # 将余额信息通过调用_save_account函数保存到json文件中
    _save_account(database)

# 定义一个函数，用于执行充值操作
def _top_up(account):
    database = _load_database()
    # 进入循环
    while True:
        # 提供交互式界面让用户输入要充值的金额
        num = input('请输入您要充值的金额:')
        # 判断如果用户输入的是不是纯数字，则将充值后的金额更新到数据库
        if num.isdigit():  # 判断输入是否为纯数字(充值的数据必须为纯数字)
            database[account]["balance"] += int(num)  # 将str格式的"纯数字"转换为int格式
            _save_account(database)  # 保存到文件
            account_balance = _get_balance(account)  # 再从文件中读取余额信息
            # 高亮打印充值后的余额信息
            print('您已成功充值,您的余额为\033[32m%d\033[0m元' % account_balance)
            # 上面已经打印余额了，所以这里定义一个return none代表不使用return的方式返回余额
            return None

        # 如果用户输入的不是纯数字，则提示输入错误，重新进行while循环，让用户重新输入
        else:
            print('您的输入有误,请重新输入!')

# 定义一个函数_get_balance，用于获取账户余额
def _get_balance(account):
    database = _load_database()
    # 将字典中账户的余额信息读取到account_balance变量
    account_balance = database[account]['balance']
    # 返回账户余额变量的值
    return account_balance

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
                    _logout(account)
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
                            _logout(account)
                        # 如果用户输入的h，则查询json文件中的购物历史
                        elif p_name == 'h':
                            database = _load_database()
                            # 有购物历史，则调用_get_shopping_history函数，输出购物历史
                            if database[account]['shopping_time'] != None:
                                _get_shopping_history()
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
                                    account_balance = _get_balance(account)
                                    # 定义一个价格变量，总价格 = 商品单价*数量，单价来自于字典，数量来自于num
                                    price = (goods[choose][c_name][p_name]) * num
                                    # 判断如果账户余额大于所购买的商品金额，才可以购买
                                    if account_balance >= price:
                                        # 调用_set_balance函数，计算购买后的账户余额是多少
                                        # #计算方法在_set_balance函数里面
                                        _set_balance(account,price)
                                        # 提示用户已经成功购买商品
                                        print('您成功购买%d件商品:%s!'% (num,p_name))
                                        # 调用_set_shopping_list函数，将购买的商品列表保存到json文件中
                                        _set_shopping_list(account,p_name,num)
                                        # 定义account_balance变量，通过使用_get_balance函数重新获取账户的余额信息
                                        account_balance = _get_balance(account)
                                        # 打印告诉用户，购买完商品之后剩下多少钱
                                        print('您目前的账户余额为\033[31m%d\033[0m元' % account_balance)
                                        # 调用_set_shopping_time函数，将购物时间写入到json文件
                                        _set_shopping_time(account)
                                        # 退出当前的循环，到上一级循环，用户可以选择是否继续购物
                                        break
                                    # 如果用户的账户余额小于商品的金额，则告诉用户余额不足，无法购买
                                    else:
                                        print('您的账户余额不足，请您及时充值！')
                                        g = input("充值输入t，返回上一级输入b，退出输入q':")
                                        if g == 'q':
                                            _logout()
                                        if g == 'b':
                                            break
                                        if g == 't':
                                        # 这里我增加了一个调用_top_up函数，账户余额不住的时候，马上提示用户充值
                                            _top_up(account)
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
            _logout(account)
        # 如果用户输入的信息既不在商品分类中，也不是q，则告诉用户重新输入
        else:
            print('输入错误，请重新输入！')

#
def _add_user():
    # 首先调用_load_database函数，将json文件解码出来，放到database变量
    database = _load_database('DataBase.json')
    # 执行while循环
    while True:
        # 提供交互式界面，让用户输入要创建的用户名称
        username = input('请输入您的账户名称：').strip()
        # 判断是否存在重名的用户，如果有，则告诉用户，继续执行while循环，让用户输入
        if username in database:
            print('用户名已经存在，不需要重复创建！')
        # 如果没有，则用户输入信息有效，中断while循环
        else:
            break
    # 执行while循环
    while True:
        # 让用户输入两次密码
        pwd1 = input('请输入您的账户密码：').strip()
        pwd2 = input('请再次输入您的账户密码：').strip()
        # 对两次输入的密码信息进行比对
        # 如果面膜不正确，则继续执行while循环让用户重新输入
        if pwd1 != pwd2:
            print('2次输入的密码不通，请重新输入')
        # 如果输入的密码是正确的，则告诉用户创建账户成功
        else:
            print('创建用户成功，开始购物吧！')
            # 把用户创建的账户和密码信息保存到database字典中
            # username为用户账号,pwd1为用户密码,balance为账户余额,shopping_list为购物清单,shopping_time为购物时间
            database[username] = {'pwd':pwd1,'balance':0,'shopping_list':[],'shopping_time':None}
            # 调用_save_account函数，将创建好的账户信息和账户的初始余额、初始购物时间信息保存到json文件
            _save_account(database)
            # 退出while循环
            break

# 设置默认变量account = None来判定账号是否已经登录,如果没有登录就退出,则不打印购物信息
# 如果已经登录过，则打印购物历史信息
def _logout(account=None):
    if account != None:
        _get_shopping_history(account)
    exit('感谢您来购物!')

# 定义一个main函数，用于初始登录界面的判断
def main():
    # 执行while循环
    while True:
        # 打印登录提示信息，info信息定义在程序的开头，是一个字符串类型
        print(info)
        # 提供交互式界面，让用户输入指令信息
        command = input('请输入指令：').strip()
        # 如果用户输入的是大写的A，则调用_add_user函数，创建新用户
        if command.upper() == 'A':
            _add_user()
        # 如果用户输入的是大写的B，则调用_login函数，进行登录
        elif command.upper() == 'B':
            _login()
        # 如果用户输入的是Q，则调用_logout函数，退出登录
        elif command.upper() == 'Q':
            _logout()
        # 如果用户没有按照提示信息进行输入，则告诉用户重新输入，会重新执行while循环
        else:
            print('输入错误，请重新输入')

# 执行main函数
if __name__ == '__main__':
    main()

























