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
2. 按"e"登录
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
                        # 调用系统模块，进行清屏操作
                        os.system('clear')
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




# 定义一个函数，用于执行充值操作
def _top_up(account):
    database = _load_database()
    while True:
        num = input('请输入您要充值的金额:')
        if num.isdigit():  # 判断输入是否为纯数字(充值的数据必须为纯数字)
            database[account]["balance"] += int(num)  # 将str格式的"纯数字"转换为int格式
            _save_account(database)  # 保存到文件
            account_balance = _get_balance(account)  # 再从文件中读取余额信息
            print('您已成功充值,您的余额为\033[32m%d\033[0m元' % account_balance)
            return None
            # shopping(account)
        else:
            print('您的输入有误,请重新输入!')

# 定义一个函数_get_balance，用于获取账户余额
def _get_balance(account):
    database = _load_database()
    account_balance = database[account]['balance']
    return account_balance

# 设置默认变量account = None来判定账号是否已经登录,如果没有登录就退出,则不打印购物信息
def _logout(account=None):
    if account != None:
        _get_shopping_history(account)
    exit('Thank you so much for coming!')

























