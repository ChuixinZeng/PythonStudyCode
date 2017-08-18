# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import xml.etree.ElementTree as ET

tree = ET.parse("xmlfile.xml")
root = tree.getroot()

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    # 给year加updated属性
    node.set("updated", "yes")

tree.write("xmlfile.xml")

# 删除node
# 循环所有的conutry，判断country下面的rank的值，如果大于50，就把country分支干掉
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')