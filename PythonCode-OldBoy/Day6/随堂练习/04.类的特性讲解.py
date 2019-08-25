# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

class Role(object): #定义一个类， class是定义类的语法，Role是类名，(object)是新式类的写法，必须这样写，以后再讲为什么
    nationality = "JP" # 公有属性
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

    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)
        '''
        member [Alex] is dead!
        member [Jack] is dead!
        member [HaiTao] is dead!
        member [LiChuang] is dead!

        '''

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

# 私有属性：self.__heart = "Normal" ，对外部不可见，无法访问，__privat_attr_name = value
# 私有属性可以达到让外面不能改只能看的效果
print(r1.get_heart()) # 安全只读访问私有属性
# 也可以强制访问私有属性，如下 r1._Role__heart


# 成员属性：只属于某个对象的，例如
r3 = Role("HaiTao","police","B22")
r4 = Role("LiChuang","Dog","B13")
print(r3.weapon) # 只属于r3的对象

# 公有属性：所有属于这个类的对象都可以访问的属性
nationality = "JP" # 公有属性，在类里直接定义的属性
print(r3.nationality)
print(r4.nationality)
# 可以通过类名直接去改公有属性
Role.nationality = "US" # 再打印就变成US了
print(r3.nationality,r4.nationality) # 结果都变成US，证明实例r3,r4跟公有属性nationality是引用的关系，而不是复制关系
# 如果再赋值
r3.nationality = "CN" # 相当于给nationality重新赋值本地变量，跟全局公有属性nationality没有关系了，只是长得一样

# 在class里面定义的def xxx()也是公有的方法，也只存了一份，比如类里面定义了def shot()这是公有方法，类外部可以再定义def shot()这可以是自己的方法

def shot2(self):
    print("this is my own shot",self.name)

r1.shot = shot2
r1.shot(r1) # this is my own shot alex
r2.shot() # Jack is shooting...

# 析构方法 def __del__(self) 在实例销毁的时候会调用