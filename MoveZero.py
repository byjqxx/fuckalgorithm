#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def move_zero(s):
    """
    给定一个数组，编写一个函数将所有的0移动到数组的末尾，同时保持非0元素的相对顺序
    请注意，尽量在不复制数组的情况下原地对数组进行操作
    """
    i = j = 0
    while i < len(s):
        if s[i] == 0:
            s.remove(s[i])
            j += 1
        i += 1

    if j > 0:
        s = s + [0 for i in range(j)]

    return s


if __name__ == "__main__":
    s = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    print(move_zero(s))