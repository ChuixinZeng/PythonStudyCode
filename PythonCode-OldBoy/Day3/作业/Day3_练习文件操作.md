### 此Readme文档是针对编写的练习文件操作的说明


### 程序基本信息

- 作者：zengchuixin
- 日期：2017/07/25
- 版本：Version 1.0
- 工具：PyCharm 2017.1.4
- 版本：Python 3.5
- MarkDown工具：HBuilder
- 流程图工具：ProcessOn

### 程序要求

- 实现针对ha_proxy文件的增删查改操作

### 输入的内容格式要求如下

		What are you do? (add|delete|search|q):add
		server info:
		{
			'backend': 'www.baidu.org',
			'record':{
				'server': '100.1.7.99',
				'weight': 20,
				'maxconn': 3
			}
		}

### 程序相关文档

- GitHub,[ChuixinZeng-Python笔记主页](https://github.com/ChuixinZeng/PythonStudyCode/tree/master/PythonCode-OldBoy/Day3)
- 博客园,[老男孩Day3作业-练习文件操作](http://www.cnblogs.com/ChuixinZeng/p/Jamie_Zeng_Day3.html)

### 2017/07/24程序优化备忘

- 无法更新文件内容的问题：修改backend内容只能在txt修改完后，粘贴到server info交互式界面里面，不要在交互式界面里面直接改，不生效，提示文件已存在，个人感觉原因是使用了inter函数，输入的内容被序列化了，然后放到str里面，再转成dict，这个时候就不能直接在交互界面修改了，要提前改好了粘贴进去

- 使用add更新文件时提示文件已存在问题：maxconn、weight的值不要和更新前的值有重合的地方，比如原始值是500，你改成50会提示文件已存在，只能改成不包含500的其他值才可以，原因是程序中使用了大量的正则表达式进行match匹配，不是严格匹配

- 用户在增加，查询，删除，更新信息的时候，交互式界面提示信息不太丰富，进行了修改
