# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 字典和列表的区别：列表是有顺序的，使用索引访问；而字典中的条目是用键来访问的

# 初始化空字典
_user_dict = {}
# 初始化空列表list,有了空的列表之后，程序就可以向这个列表中增加元素
_user_list = []
# 初始化登录不存在用户名的初始值为0
_login_error_count = 0

# 使用while开始无限制的循环
while True:
    # 交互式输入登录用户名和密码
    _user_naming = input("Pls input your username:")
    _user_password = input("Pls input your password:")
    # 读取用户登录数据文件UserPassword.txt
    _users_data = open('UserPassword.txt')
    # 循环遍历打开的数据，对打开的数据进行格式化操作，然后把格式化以后的数据保存到创建好的_user_dict字典当中
    for user_data in _users_data:
        # 使用strip去除user_data数据行中的前后空格
        _user_list = user_data.strip()
        # 将去除前后空格之后的数据行_user_list使用逗号进行分割，并重新保存到_user_datas中
        _user_datas = _user_list.split(',')
        # 将_user_datas数据行中的第0个位置的数据（即用户名），去除前后空格后，赋给新的变量_user_name
        _user_name = _user_datas[0].strip()
        # 将_user_datas数据行中的第1个位置的数据（即密码），去除前后空格后，赋给新的变量_user_pass
        _user_pass = _user_datas[1].strip()
        # 将_user_datas数据行中的第2个位置的数据（即锁定状态，0代表未锁定，1代表锁定），去除前后空格后，赋给新的变量_user_locked
        _user_locked = _user_datas[2].strip()
        # 将_user_datas数据行中的第3个位置的数据（即密码输入错误次数），去除前后空格后，赋给新的变量_user_error_count
        # 将_user_datas[3]的数据类型强制转换为int
        _user_error_count = int(_user_datas[3].strip())
        # 将前面定义好的变量信息，保存到字典中，为前面的值指定键名，即键：值对应的关系，键名可以随便起，建议考虑易读性
        # 如果下面的键名出线下划波浪线，并不代表有语法错误，而是编辑器认为拼写的英文不是正确的英文单词，不影响脚本执行
        # 按照Python的编程规范，在逗号和冒号后面需要加一个空格
        _user_dict[_user_name] = {'name': _user_name, 'password': _user_pass,
                                  'locked': _user_locked, 'errorcount': _user_error_count}

    # 关闭打开的UserPassword.txt文件
    _users_data.close()

    # 判断用户账户是否已经被锁定，将前面交互界面输入的用户名和字典里保存的用户名列进行匹配
    # 将前面交互式输入的用户名和字典中的userlocked键进行匹配，如果用户名对应的键为1，就是被锁定了，退出登录
    if _user_naming in _user_dict.keys():
        if _user_dict[_user_naming]['locked'] == '1':
            print("The account was locked,pls contact administrator!")
            break
        # 将前面输入的用户名、密码和字典中的用户名、密码进行匹配，如果成功，则输出登录系统，然后退出
        if _user_naming == _user_dict[_user_naming]['name'] and _user_password == _user_dict[_user_naming]['password']:
            print("Welcome to System!")
            break
        else:
            # 如果用户名在字典里，但是密码不对，将前面输入的用户名所对应字典中的错误次数进行自增
            _user_dict[_user_naming]['errorcount'] += 1
            # 如果用户名输入正确的情况下，密码输入错误的次数小于3次，给用户重新尝试的机会
            if _user_dict[_user_naming]['errorcount'] < 3:
                print("The password was wrong,pls try again,your have three chance!")
                # 追加写入新的数据到UserPassword.txt，其中的errorcount会随着失败尝试次数的增加而增加，三次就是2，即0,1,2
                _write_data = open('UserPassword.txt', 'w+')
                # 将字典里面的值取到_user_value中，进行循环遍历
                for _user_value in _user_dict.values():
                    # 往脚本开头定义好的空列表里面逐行写入数据
                    _user_list = [_user_value['name'], _user_value['password'], str(_user_value['locked']),
                                  str(_user_value['errorcount'])]
                    # 将写入到_user_list的数据再次进行格式化后赋给_users_list
                    _users_list = ','.join(_user_list)
                    # 将_users_list中的数据写入到UserPassword.txt中，并在每一行数据的结尾进行换行
                    _write_data.write(_users_list + '\n')
                # 关闭UserPassword.txt文档
                _write_data.close()

            else:
                # 如果密码不正确的次数已经超过3次，就输出账户被锁定
                print("You try three times,Account locked")
                # 输出账户锁定的同时，将字典中locked键的值设置为1，这个地方改成1，前面判断Locked状态的IF才生效
                _user_dict[_user_naming]['locked'] = 1
                # 账户设置为锁定之后，将用户对应的错误密码次数清零，我理解的是锁定属性为1了，错误次数可以清零
                _user_dict[_user_naming]['errorcount'] = 0
                _write_data = open('UserPassword.txt', 'w+')
                for _user_value in _user_dict.values():
                    _user_list = [_user_value['name'], _user_value['password'], str(_user_value['locked']),
                                  str(_user_value['errorcount'])]
                    _users_list = ','.join(_user_list)
                    _write_data.write(_users_list + '\n')
                _write_data.close()
                break


    else:
        # 如果用户名不存在，则输出信息
        print("Pls ensure input currect account or password,you can try three times!")
        # 程序开头设置了初始化不存在用户名的值为0，这里进行自增
        _login_error_count += 1
        # 如果不存在的用户尝试次数超过3次，则中断程序
        if _login_error_count > 2:
            break


