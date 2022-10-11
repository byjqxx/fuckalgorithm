#!/usr/bin/env python
# *-* coding:utf-8 *-*

def get_factor(num: int):
    """
    求一个数所有的因数
    """
    i = 1
    factors = []
    while i <= num:
        if num % i == 0:
            factors.append(i)
        i += 1
    for f in factors:
        print(f)


if __name__ == "__main__":
    n = int(input())
    get_factor(n)