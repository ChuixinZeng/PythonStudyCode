# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

'''

面向对象编程 (OOP) 语言的一个主要功能就是“继承”。继承是指这样一种能力：它可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。

通过继承创建的新类称为“子类”或“派生类”。

被继承的类称为“基类”、“父类”或“超类”。

继承的过程，就是从一般到特殊的过程。

要实现继承，可以通过“继承”（Inheritance）和“组合”（Composition）来实现。

在某些 OOP 语言中，一个子类可以继承多个基类。但是一般情况下，一个子类只能有一个基类，要实现多重继承，可以通过多级继承来实现。

继承概念的实现方式主要有2类：实现继承、接口继承。

Ø         实现继承是指使用基类的属性和方法而无需额外编码的能力；
Ø         接口继承是指仅使用属性和方法的名称、但是子类必须提供实现的能力(子类重构爹类方法)；
在考虑使用继承时，有一点需要注意，那就是两个类之间的关系应该是“属于”关系。例如，Employee 是一个人，Manager 也是一个人，
因此这两个类都可以继承 Person 类。但是 Leg 类却不能继承 Person 类，因为腿并不是一个人。

抽象类仅定义将由子类创建的一般属性和方法。
OO开发范式大致为：划分对象→抽象类→将类组织成为层次化结构(继承和合成) →用类与实例进行设计和实现几个阶段。

'''

# 命名规范：类名首字母大写，函数名全部小写即可
class SchoolMember(object):
    members = 0  # 初始学校人数为0,公有属性，每注册一个人加1

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

    def enroll(self):
        '''注册'''
        SchoolMember.members += 1
        print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " % (
        self.name, SchoolMember.members))

    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)


class Teacher(SchoolMember):
    '''讲师类'''
    def __init__(self, name, age, sex, course, salary):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.salary = salary
        self.enroll() # 自动计数

    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, 'Oldboy', self.course)
        print(msg)


class Student(SchoolMember):
    '''学生类'''
    def __init__(self, name, age, sex, grade, sid):
        SchoolMember.__init__(self, name, age, sex)
        self.grade = grade
        self.sid = sid
        self.enroll()
        self.amount = 0

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, 'Oldboy')
        print(msg)

    def pay_tuition(self,amount):
        '''交钱'''
        print("student [%s] has just paied [%s]" %(self.name, amount))
        self.amount += amount


if __name__ == '__main__':

    t1 = Teacher("Alex", 22, "FM",'Python', 20000)
    t2 = Teacher("TengLan", 29,"FM",'Linux', 3000)

    s1 = Student("Qinghua", 24, "FM", "Python S12", 1483)
    s2 = Student("SanJiang", 26, "FM", "Python S12", 1484)

    t1.teaching()
    t2.teaching()
    t1.tell()

    '''result'''
    '''
new member [Alex] is enrolled,now there are [1] members. 
new member [TengLan] is enrolled,now there are [2] members. 
new member [Qinghua] is enrolled,now there are [3] members. 
new member [SanJiang] is enrolled,now there are [4] members. 
Teacher [Alex] is teaching [Python] for class [s12]
Teacher [TengLan] is teaching [Linux] for class [s12]
Hi, my name is [Alex], works for [Oldboy] as a [Python] teacher !
member [Alex] is dead!
member [TengLan] is dead!
member [Qinghua] is dead!
member [SanJiang] is dead!
    
    '''