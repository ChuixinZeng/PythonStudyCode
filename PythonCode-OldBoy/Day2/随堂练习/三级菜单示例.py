# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
# 三级菜单，所以加了三层死循环
exit_flag = False

while not exit_flag:
    for i in menu:
        print(i) #打印第一层菜单
    choose = input("选择进入>>>：")
    if choose in menu:
        while not exit_flag:
            for i2 in menu[choose]:
                print("\t",i2) # 打印第二层菜单
            choose2 = input("选择输入：")
            if choose2 in menu[choose]:
                while not exit_flag:
                    for i3 in menu[choose][choose2]:
                        print("\t",i3) # 打印第三层菜单
                    choose3 = input("选择进入3级：")
                    if choose3 in menu[choose][choose2]:
                        for i4 in menu[choose][choose2][choose3]:
                            print("\t\t",i4) # 打印第四层菜单
                        choose4 = input("最后一层，b 返回：")
                        if choose4 == "b":
                            pass # 相当于什么也不做，相当于占位符，让代码不出错
                        elif choose4 == "q":
                            exit_flag = True

                    if choose3 == "b":
                        break
                    elif choose3 == "q":
                        exit_flag = True

            if choose2 == "b":
                break
            elif choose2 == "q":
                exit_flag = True
    if choose == "q":
        break