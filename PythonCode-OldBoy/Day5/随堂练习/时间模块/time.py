# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import time
# 元组（struct_time）共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同
# weekday代表一周的第几天，比如weekday=5，代表一周的第六天，即周六
print(time.localtime())

# 不会使用查看帮助信息
# print(help(time))

# 从输出的time里面取值
# 输出时间日期为struct_time元组形式
x = time.localtime()
print(x)

# 不知道如何取值，可以先查x的方法
# print(help(x))
print(x.tm_year)
print('this is 2017 day:%d' %x.tm_yday)

# 将时间戳转换成struct_time元组形式
# 结果time.struct_time(tm_year=1973, tm_mon=11, tm_mday=27, tm_hour=9, tm_min=52, tm_sec=3, tm_wday=1, tm_yday=331, tm_isdst=0)
print(time.localtime(123213123))

# 将struct_time元组形式转换为格式化字符串形式
# 格式化时间，月份要使用小写的m，否则会显示成后面大M代表的分钟Minute
print(time.strftime("%Y-%m-%d %H:%M:%S",x))

# 将格式化的时间转换为struct_time元组的格式
# 下面的string和format的位置必须一一对应
print(time.strptime('2017-08-18 11:34:36','%Y-%m-%d %H:%M:%S'))

# print(time.clock()) #返回处理器时间,3.3开始已废弃 , 改成了time.process_time()测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
# print(time.altzone)  #返回与utc时间的时间差,以秒计算\
# print(time.asctime()) #返回时间格式"Fri Aug 19 11:14:16 2016",
# print(time.localtime()) #返回本地时间 的struct time对象格式
# print(time.gmtime(time.time()-800000)) #返回utc时间的struc时间对象格式

# print(time.asctime(time.localtime())) #返回时间格式"Fri Aug 19 11:14:16 2016",
# print(time.ctime()) #返回Fri Aug 19 12:38:29 2016 格式, 同上



# 日期字符串 转成  时间戳
# string_2_struct = time.strptime("2016/05/22","%Y/%m/%d") #将 日期字符串 转成 struct时间对象格式
# print(string_2_struct)
# #
# struct_2_stamp = time.mktime(string_2_struct) #将struct时间对象转成时间戳
# print(struct_2_stamp)

'''
%a    本地（locale）简化星期名称    
%A    本地完整星期名称    
%b    本地简化月份名称    
%B    本地完整月份名称    
%c    本地相应的日期和时间表示    
%d    一个月中的第几天（01 - 31）    
%H    一天中的第几个小时（24小时制，00 - 23）    
%I    第几个小时（12小时制，01 - 12）    
%j    一年中的第几天（001 - 366）    
%m    月份（01 - 12）    
%M    分钟数（00 - 59）    
%p    本地am或者pm的相应符    一    
%S    秒（01 - 61）    二    
%U    一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。    三    
%w    一个星期中的第几天（0 - 6，0是星期天）    三    
%W    和%U基本相同，不同的是%W以星期一为一个星期的开始。    
%x    本地相应日期    
%X    本地相应时间    
%y    去掉世纪的年份（00 - 99）    
%Y    完整的年份    
%Z    时区的名字（如果不存在为空字符）    
%%    ‘%’字符

'''
'''
NAME
    time - This module provides various functions to manipulate time values.

DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).
    
    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
    
    Variables:
    
    timezone -- difference in seconds between UTC and local standard time
    altzone -- difference in  seconds between UTC and local DST time
    daylight -- whether local time should reflect DST
    tzname -- tuple of (standard time zone name, DST time zone name)
    
    Functions:
    
    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone

CLASSES
    builtins.tuple(builtins.object)
        struct_time
    
    class struct_time(builtins.tuple)
     |  The time value as returned by gmtime(), localtime(), and strptime(), and
     |  accepted by asctime(), mktime() and strftime().  May be considered as a
     |  sequence of 9 integers.
     |  
     |  Note that several fields' values are not the same as those defined by
     |  the C language standard for struct tm.  For example, the value of the
     |  field tm_year is the actual year, not year - 1900.  See individual
     |  fields' descriptions for details.
     |  
     |  Method resolution order:
     |      struct_time
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  tm_hour
     |      hours, range [0, 23]
     |  
     |  tm_isdst
     |      1 if summer time is in effect, 0 if not, and -1 if unknown
     |  
     |  tm_mday
     |      day of month, range [1, 31]
     |  
     |  tm_min
     |      minutes, range [0, 59]
     |  
     |  tm_mon
     |      month of year, range [1, 12]
     |  
     |  tm_sec
     |      seconds, range [0, 61])
     |  
     |  tm_wday
     |      day of week, range [0, 6], Monday is 0
     |  
     |  tm_yday
     |      day of year, range [1, 366]
     |  
     |  tm_year
     |      year, for example, 1993
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 9
     |  
     |  n_sequence_fields = 9
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.

FUNCTIONS
    asctime(...)
        asctime([tuple]) -> string
        
        Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
        When the time tuple is not present, current time as returned by localtime()
        is used.
    
    clock(...)
        clock() -> floating point number
        
        Return the CPU time or real time since the start of the process or since
        the first call to clock().  This has as much precision as the system
        records.
    
    ctime(...)
        ctime(seconds) -> string
        
        Convert a time in seconds since the Epoch to a string in local time.
        This is equivalent to asctime(localtime(seconds)). When the time tuple is
        not present, current time as returned by localtime() is used.
    
    get_clock_info(...)
        get_clock_info(name: str) -> dict
        
        Get information of the specified clock.
    
    gmtime(...)
        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                               tm_sec, tm_wday, tm_yday, tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.
        
        If the platform supports the tm_gmtoff and tm_zone, they are available as
        attributes only.
    
    localtime(...)
        localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                  tm_sec,tm_wday,tm_yday,tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing local time.
        When 'seconds' is not passed in, convert the current time instead.
    
    mktime(...)
        mktime(tuple) -> floating point number
        
        Convert a time tuple in local time to seconds since the Epoch.
        Note that mktime(gmtime(0)) will not generally return zero for most
        time zones; instead the returned value will either be equal to that
        of the timezone or altzone attributes on the time module.
    
    monotonic(...)
        monotonic() -> float
        
        Monotonic clock, cannot go backward.
    
    perf_counter(...)
        perf_counter() -> float
        
        Performance counter for benchmarking.
    
    process_time(...)
        process_time() -> float
        
        Process time for profiling: sum of the kernel and user-space CPU time.
    
    sleep(...)
        sleep(seconds)
        
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.
    
    strftime(...)
        strftime(format[, tuple]) -> string
        
        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    strptime(...)
        strptime(string, format) -> struct_time
        
        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as
        strftime()).
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    time(...)
        time() -> floating point number
        
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.

DATA
    altzone = -32400
    daylight = 0
    timezone = -28800
    tzname = ('ÖÐ¹ú±ê×¼Ê±¼ä', 'ÖÐ¹úÏÄÁîÊ±')

FILE
    (built-in)


None

Process finished with exit code 0
'''