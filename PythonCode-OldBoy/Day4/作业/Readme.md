### 程序基本信息

- 作者：zengchuixin
- 日期：2017/08/09
- 版本：Version 1.0
- 工具：PyCharm 2017.1.4
- 版本：Python 3.5
- MarkDown工具：HBuilder
- 流程图工具：ProcessOn

### 程序要求

- 实现增删改查操作：
- 可进行模糊查询，语法至少支持下面3种:
    select name,age from staff_table where age > 22
    select from staff_table where dept = "IT"
    select from staff_table where enroll_date like "2013"
- 查到的信息，打印后，最后面还要显示查到的条数
- 可创建新员工纪录，以phone做唯一键，staff_id需自增
- 可删除指定员工信息纪录，输入员工id，即可删除
- 可修改员工信息，语法如下:
    UPDATE staff_table SET dept = "Market" WHERE where dept = "IT"
		staff_id,name,age,phone,dept,enroll_date
		1,Alex Li,22,13651054608,IT,2013-04-01
		2,Jack Wang,30,13304320533,HR,2015-05-03
		3,Rain Liu,25,1383235322,Sales,2016-04-22
		4,Mack Cao,40,1356145343,HR,2009-03-01
- 注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码 

### 设计思路流程图

- GitHub,[Day4_员工信息表程序_流程图](https://github.com/ChuixinZeng/PythonStudyCode/blob/master/PythonCode-OldBoy/Day4/作业/Day4_员工信息表程序_流程图.png)

### 程序相关文档

- GitHub,[Day4所有代码笔记](https://github.com/ChuixinZeng/PythonStudyCode/tree/master/PythonCode-OldBoy/Day4)
- 博客园,[老男孩Day4作业：员工信息表程序](http://www.cnblogs.com/ChuixinZeng/p/Jamie_Zeng_Day4.html)