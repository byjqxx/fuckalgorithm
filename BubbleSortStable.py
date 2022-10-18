#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def bubble_sort_stable(s):
    for i in range(len(s)):
        for j in range(len(s)-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                print("第 %d 轮第 %d 次排序， s[%d] 与 s[%d] 交换后：" % (i+1, j+1, j,
                                                             j+1), s)
    return s


if __name__ == "__main__":
    s = [10, 8, 9, 9, 7, 6, 5, 4, 3, 2, 1]
    print("before sort：", s)
    s1 = bubble_sort_stable(s)
    print("after sort：", s1)
