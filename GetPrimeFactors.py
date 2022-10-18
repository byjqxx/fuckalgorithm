#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def get_prime_factors(n):
    """
    求一个数的所有质因数
    """
    while n % 2 == 0:
        print(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while (n % i) == 0:
            print(i)
            n = n // i

    if n > 2:
        print(n)


if __name__ == "__main__":
    num = 650
    get_prime_factors(num)