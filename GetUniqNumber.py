#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def get_uniq_number(s):
    """
    给定一个整数数组，数组中有一个数出现了一次，其他数出现了两次，请找出只出现了一次的数。
    """
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]


def get_uniq_number2(s):
    s = sorted(s)
    i = 0
    while i < len(s):
        if s[i] != s[i+1]:
            return s[i]
        else:
            i += 2


if __name__ == "__main__":
    s = [1, 1, 2, 2, 3, 3, 4, 8, 8, 5, 5]
    #print(get_uniq_number(s))
    print(get_uniq_number2(s))