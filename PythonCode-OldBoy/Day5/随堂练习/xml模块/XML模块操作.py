# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

# 跟json差不多，但JSON更简单，在json没诞生的时候，只能用XML
# xml协议在各个语言里的都 是支持的，在python中可以用以下模块操作xml 　

import xml.etree.ElementTree as ET

tree = ET.parse("xmlfile.xml")
root = tree.getroot()
print("roottag:",root.tag)

# 遍历xml文档
for child in root:
    print("childtag and childattrib:",child.tag, child.attrib)
    for i in child:
        print("itag and itext:",i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)