# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

class SchoolMember(object):
    members = 0  # 初始学校人数为0

    def __init__(self, name, age):
        self.name = name
        self.age = age

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

class School(object):
    '''学校类，演示多重继承'''
    def Open_branch(self,addr):
        print("openning a new branch in ", addr)


class Teacher(SchoolMember,School): # 多重继承，teacher同时继承了SchoolMember和School，用的地方不多
    def __init__(self, name, age, course, salary):
        super(Teacher, self).__init__(name, age) # 新式类继承写法
        self.course = course
        self.salary = salary
        self.enroll()

    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, 'Oldboy', self.course)
        print(msg)


class Student(SchoolMember):
    def __init__(self, name, age, grade, sid):
        super(Student, self).__init__(name, age) # 新式类继承写法
        self.grade = grade
        self.sid = sid
        self.enroll()

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, 'Oldboy')
        print(msg)


if __name__ == '__main__':
    t1 = Teacher("Alex", 22, 'Python', 20000)
    t2 = Teacher("TengLan", 29, 'Linux', 3000)

    s1 = Student("Qinghua", 24, "Python S12", 1483)
    s2 = Student("SanJiang", 26, "Python S12", 1484)

    t1.teaching()
    t2.teaching()
    t1.tell()
    t1.Open_branch("SH") # 多重继承的结果，teacher同时继承了SchoolMember和School

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