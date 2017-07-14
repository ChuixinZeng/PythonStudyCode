# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

# 更新字典里面的值
av_catalog["大陆"]["1024"][1] = "可以在国内做镜像"
print(av_catalog["大陆"])

# 键尽量不要写中文，可能出现编码不一致的问题

# 打印所有的值，取第一层键的值
print(av_catalog.values())
# 打印所有的键
print(av_catalog.keys())

# 插入新的键值，会先到字典里面尝试取台湾的值，如果取到就返回，如果取不到就创建新值
av_catalog.setdefault("台湾",{"www.baidu.com":[1,2]})


