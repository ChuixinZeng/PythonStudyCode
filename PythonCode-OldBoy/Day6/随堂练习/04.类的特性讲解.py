# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

class Role(object): #定义一个类， class是定义类的语法，Role是类名，(object)是新式类的写法，必须这样写，以后再讲为什么
    def __init__(self,name,role,weapon,life_value=100,money=15000): #初始化函数，在生成一个角色时要初始化的一些属性就填写在这里
        self.name = name #__init__中的第一个参数self,和这里的self都 是什么意思？ 看下面解释
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__heart = "Normal" # 私有属性

    def get_heart(self):
        return self.__heart # 私有属性可以达到让外面不能改只能看的效果

    def shot(self):
        print("%s is shooting...." % self.name)

    def got_shot(self):
        print("I got shot...")
        self.__heart = "DIE" # 私有属性内部是可见的
        print(self.__heart) # 正常打印私有属性

    def buy_gun(self,gun_name):
        print("%s just bought %s" % (self.name,gun_name))
        self.weapon = gun_name
        # 当buy_gun的值（B21）和Role里面的值（AK47)不一致时,强制使用buy_gun的值

r1 = Role('Alex','police','AK47') #生成一个角色 , 会自动把参数传给Role下面的__init__(...)方法
r2 = Role('Jack','terrorist','B22') #生成一个角色

r1.shot()
r1.buy_gun("B21”) #python 会自动帮你转成 Role.buy_gun(r1,”B21")
# print（r1.__heart) # 无法打印私有属性，会报错
# #Alex has just bought B21


# r1 = Role('Alex','police','AK47’) #此时self 相当于 r1 ,  Role(r1,'Alex','police','AK47’)
# r2 = Role('Jack','terrorist','B22’)#此时self 相当于 r2, Role(r2,'Jack','terrorist','B22’)

# 类——》实例化——》实例对象
# __init__ 构造函数
# self.name = name 属性或者成员变量
# def sayhi() 方法又叫做动态属性
# 公有属性：
# 私有属性：self.__heart = "Normal" ，对外部不可见，无法访问，__privat_attr_name = value
# 私有属性可以达到让外面不能改只能看的效果
print(r1.get_heart())
# 也可以强制访问私有属性，如下 r1._Role__heart
