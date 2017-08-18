# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist") # 这就是根节点
Personinfo = ET.SubElement(new_xml, "Personinfo", attrib={"enrolled": "yes"}) # subelement是子节点，创建根节点的子节点
name = ET.SubElement(Personinfo,"name")
name.text = "zengchuixin"
age = ET.SubElement(Personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(Personinfo, "sex")
age.text = '33'
Personinfo2 = ET.SubElement(new_xml, "Personinfo", attrib={"enrolled": "no"})
age = ET.SubElement(Personinfo2, "age")
age.text = '19'
name = ET.SubElement(Personinfo2,"name")
name.text = "zengchuixin100"

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True) # xml_declaration声明是xml格式的

ET.dump(new_xml)  # 打印生成的格式