#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    对一个数据a进行分类，分类方法为：此数据a（四个字节大小）的四个字节相加 % 一个给定的值，如果得到的结果小于一个给定的值c，则此结果即为数据a的类型；如果得到的结果大于或者等于c，则此结果无效即为数据a的类型无效。

比如一个数据a = 0x01010101，b = 3，按照分类方法计算（0x01 + 0x01 + 0x01 + 0x01）% 3 = 1。所以如果 c = 2，则此a的类型是1，如果c = 1，则此a的类型是无效。

现给定c = 5，b = 2，数据 a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}。计算数据最多的类型（有效类型）有多少个数据。（答案为5）
https://blog.csdn.net/juge0007/article/details/82223053
"""


nums = input()
c = int(nums.split()[0])
b = int(nums.split()[1])
data = [ int(n) for n in nums.split()[2:] ]

dict1 = {}
for i in data:
    i_ = hex(i)[2:].zfill(8)
    temp = 0

    for i in range(0, len(i_), 2):
        temp += int(i_[i:i+2], 16)

    t = temp % b
    if t < c:
        if t in dict1:
            dict1[t] += 1
        else:
            dict1[t] = 1

if dict1:
    print(max(dict1.values()))
else:
    print(0)