# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 使用字典保存省份、市、县列表
# 这是一个多级的字典，可以通过for查询每一个级别的信息，级别：省份、市、区

_country_dict = {
    '1.河南省': {
        '1.郑州市': {'1.金水区': ['区号100', '邮编400000'], '2.中原区': ['区号101', '邮编400001'], '3.二七区': ['区号102', '邮编400002']},
        '2.洛阳市': {'1.老城区': ['区号200', '邮编200000'], '2.洛龙区': ['区号201', '邮编200001'], '3.西工区': ['区号203', '邮编200002']},
        '3.信阳市': {'1.浉河区': ['区号300', '邮编300000'], '2.平桥区': ['区号301', '邮编300001'], '3.固始区': ['区号203', '邮编200002']}
    },
    '2.河北省': {
        '1.石家庄市': {'1.长安区': ['区号400', '邮编500000'], '2.新华区': ['区号401', '邮编500001'], '3.桥西区': ['区号402', '邮编500002']},
        '2.保定市': {'1.竞秀区': ['区号500', '邮编600000'], '2.莲池区': ['区号501', '邮编600001'], '3.满城区': ['区号503', '邮编600002']},
        '3.邯郸市': {'1.丛台区': ['区号600', '邮编700000'], '2.邯山区': ['区号601', '邮编700001'], '3.复兴区': ['区号602', '邮编700002']}
    },
    '3.湖南省': {
        '1.长沙市': {'1.芙蓉区': ['区号700', '邮编800000'], '2.岳麓区': ['区号701', '邮编800001'], '3.雨花区': ['区号702', '邮编800002']},
        '2.常德市': {'1.武陵区': ['区号800', '邮编900000'], '2.鼎城区': ['区号801', '邮编900001'], '3.未知区': ['区号803', '邮编900002']},
        '3.湘潭市': {'1.丛台区': ['区号900', '邮编110000'], '2.邯山区': ['区号901', '邮编110001'], '3.复兴区': ['区号902', '邮编110002']}
    },
    '4.湖北省': {
        '1.武汉市': {'1.江岸区': ['区号110', '邮编810000'], '2.江汉区': ['区号111', '邮编810001'], '3.汉阳区': ['区号112', '邮编810002']},
        '2.宜昌市': {'1.西陵区': ['区号120', '邮编910000'], '2.点军区': ['区号121', '邮编910001'], '3.夷陵区': ['区号123', '邮编910002']},
        '3.孝感市': {'1.孝南区': ['区号130', '邮编120000'], '2.孝感区': ['区号131', '邮编120001'], '3.未知区': ['区号132', '邮编120002']}
    }
}


# 定义一个函数，用于将查询到的省份信息传递给此函数

def district():
    while True:
        # 定义一个空列表，用于保存城市信息
        cy = []
        # %s是处理对象的一种方法，是占位符，它的值来源于后面的% province省份的值，然后通过print打印出来
        # province的值是在查询身份的语句里面定义的
        print('%s 有以下城市：' % province)
        # 通过for循环将用户选择的省份下面的城市列表放到_city中
        for _city in sorted(_country_dict[province].keys()):
            # 打印用户选择的省份下面的城市的列表
            print(_city)
            # 将用户选择的省份下面的城市列表附加保存到cy列表中
            cy.append(_city)
        # print(cy)
        # 提供交互式界面，让用户输入要查询的城市编号
        _city_number = input('请输入要查询的城市编号：（后退：b 退出：q)')
        # 打印城市和区县列表的分隔符
        print('---------------------------------------------------')
        # 如果用户输入的编号是q，则退出查询
        if _city_number == 'q':
            print('已退出查询！')
            exit()
        # 如果用户输入的是b，则中断当前的判断，退回到上一级省份目录
        elif _city_number == 'b':
            break
        else:
            # 如果用户输入的是正确的编号，则从cy城市列表中获取到城市信息，放到city中
            for city in cy:
                # 判断用户输入的城市编号和cy列表中的城市编号是否匹配
                if _city_number in city:
                    # 如果匹配，则将当前城市的名称保存到_citynumber变量中
                    _citynumber = city
                    # %s是处理对象的一种方法，是占位符，它的值来源于% _citynumber具体城市的值，然后通过print打印出来
                    print('%s 该城市有下列区县：' % _citynumber)

                    # 通过while循环，将具体城市下面的区县信息查出来
                    while True:
                        # 用于保存区县信息的列表
                        n = []
                        # 通过for循环将用户选择的城市下面的区县列表放到_districts中
                        for _districts in sorted(_country_dict[province][_citynumber].keys()):
                            # 打印区县的名称信息，例如二七区
                            print(_districts)
                            # 将区县信息保存到n列表中
                            n.append(_districts)
                        # 提供交互式界面，让用户输入区县的查询行为
                        _phone_number = input('请输入要查询的区县的编号：（后退：b 退出：q）')
                        # # 打印区县和区县具体信息列表的分隔符
                        print('---------------------------------------------------')
                        # 如果用户输入了q，则结束查询
                        if _phone_number == 'q':
                            print('已结束查询！')
                            exit()
                        # 如果用户输入了b，则返回到上一级查询
                        elif _phone_number == 'b':
                            break  # 跳出当前循环，回到上一级循环
                        else:
                            # 通过循环遍历从区县列表n中读取区县信息到pn中
                            for pn in n:
                                # 如果用户输入的区县编号和pn中的区县编号匹配
                                if _phone_number in pn:
                                    # 则将具体匹配到的区县的名称保存到phone_number中
                                    phone_number = pn
                                    # %s的值来源于% _phone_number具体区县的值，然后通过print打印出来
                                    print('%s 的信息如下：' % phone_number)
                                    # 通过for循环将用户选择的具体的区县的列表中的信息放到p中
                                    for p in _country_dict[province][_citynumber][phone_number]:
                                        # 打印具体区县下面的邮政编码和区号信息
                                        print(p)
                                    # 打印查询分隔符
                                    print('---------------------------------------------------')
                                    # 通过交互式界面询问用户，是否继续查询
                                    _end_get = input('查询已完成，是否继续其他查询？（继续：Y 其他：结束）')
                                    # 如果用户输入的是大写的Y，则返回到上一级继续查询
                                    if _end_get == 'Y':
                                        break
                                    # 如果用户输入除了大写Y以外其他的值，则结束查询
                                    else:
                                        print('已结束查询！')
                                        exit()
                            # 如果用户输入的区县编号有误，提示用户重新输入
                            else:
                                print('区县编号输入错误，请重新输入')
                    # 第三个while True循环的退出
                    break
    # 如果用户输入的城市编号不对，则提示用户重新输入
    else:
        print('城市编号输入有误，请重新输入！')
    # 第二个while True不设置中断条件，用户可以退回到当前的城市查询列表中

while True:

    # 初始化空列表，用于保存省份信息
    c = []
    # 从国家字典中取第一级列表每一行的值，循环放到_country中
    for _country in sorted(_country_dict.keys()):
        # 逐行输出国家字典里第一级列表每一行的值
        print (_country)
        '''
        打印效果
        1.河南省
        2.河北省
        3.湖南省
        4.湖北省
    '''
        # 将取到的第一级列表每一行的值追加放入c列表中
        c.append(_country)
    # print(c) # c列表打印的结果['1.河南省', '2.河北省', '3.湖南省', '4.湖北省']
    # 提供交互式界面给用户输入省份编号信息
    country_number = input("请输入要查询的省份编号：（退出：q）")
    # 打印省份和城市分割线
    print('---------------------------------------------------')
    # 如果用户输入的是q，则退出查询
    if country_number == 'q':
        print('已退出查询！')
        break

    # 如果没有输入q，则有两种情况：1）查询到身份列表，则把省份信息传递给district()函数做进一步查询；2）提示用户输入的编号有错误
    else:
        # 遍历c列表中的省份信息，保存到country中
        for country in c:
            if country_number in country:
                # 将遍历到的C列表的省份信息同用户输入的省份编号进行对比
                # 如果输入的编号和省份编号一致，则把country的值赋予给province，从而方便进一步查询特定省份下面的城市列表
                province = country
                # 如果符合上面的条件，则开始执行函数，此函数的目的是在现有查询的基础上进一步查询城市和区县信息
                district()
                # print(country_number) # 测试用户交互式输入信息
                break
        else:
            print("您输入的省份编号有误，请重新输入！")
# 第一个while True不设置中断条件，用户可以退回到当前的身份查询列表中












