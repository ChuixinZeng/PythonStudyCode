# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]


def binary_search(dataset, find_num):
    print(dataset)

    if len(dataset) > 1:
        mid = int(len(dataset) / 2)
        if dataset[mid] == find_num:  # find it
            print("找到数字", dataset[mid])
        elif dataset[mid] > find_num:  # 找的数在mid左面
            print("\033[31;1m找的数在mid[%s]左面\033[0m" % dataset[mid])
            return binary_search(dataset[0:mid], find_num)
        else:  # 找的数在mid右面
            print("\033[32;1m找的数在mid[%s]右面\033[0m" % dataset[mid])
            return binary_search(dataset[mid + 1:], find_num)
    else:
        if dataset[0] == find_num:  # find it
            print("找到数字啦", dataset[0])
        else:
            print("没的分了,要找的数字[%s]不在列表里" % find_num)


binary_search(data, 66)