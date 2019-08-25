# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 新式类写法：class Person(object):
# 新式类继承的写法：super(Teacher, self).__init__(name, age)
# 目前主要是使用新式类的写法，object是基类，查看object的帮助信息如下：
'''
class object:
    """ The most base type """

    def __delattr__(self, *args, **kwargs):  # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs):  # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs):  # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs):  # real signature unknown
        """
        This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self):  # known special case of object.__init__
        """ Initialize self.  See help(type(self)) for accurate signature. """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(cls, *more):  # known special case of object.__new__
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs):  # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs):  # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs):  # real signature unknown
        """ Return str(self). """
        pass

    @classmethod  # known case
    def __subclasshook__(cls, subclass):  # known special case of object.__subclasshook__
        """
        Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    __class__ = None  # (!) forward: type, real value is ''
    __dict__ = {}
    __doc__ = ''
    __module__ = ''

'''



# 经典类写法：class Person:
# 经典类继承的写法：SchoolMember.__init__(self, name, age, sex)

# 新式类继承的顺序（示例）

# 示例一

'''
class A(object):
    def __init__(self):
        self.n = "A"

class B(A):
    def __init__(self):
        self.n = "B"

class C(A):
    def __init__(self):
        self.n = "C"

class D(B,C):
    def __init__(self):
        self.n = "D"

d = D()
print(d.n) # 结果是D
'''

# 示例二

'''
class A(object):
    def __init__(self):
        self.n = "A"

class B(A):
    def __init__(self):
        self.n = "B"

class C(A):
    def __init__(self):
        self.n = "C"

class D(B,C):
    pass

d = D()
print(d.n) # 结果是B

'''

# 示例三

'''
class A(object):
    def __init__(self):
        self.n = "A"

class B(A):
    pass

class C(A):
    def __init__(self):
        self.n = "C"

class D(B,C):
    pass

d = D()
print(d.n) # 结果是C
'''

# 结论：
# 1. 新式类寻找的顺序是D/B/C/A，术语叫做“广度查找”
# 2. 如果在Python2里面再次执行上面的代码，顺序是有区别的D/B/A/C，这种查询叫做“深度查找”
# 3. 在Python3里面全部都是广度查找





