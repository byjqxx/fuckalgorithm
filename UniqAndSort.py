"""
输入描述：
第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数。
输出描述：
输出多行，表示输入的N个数去重排序处理后的结果
"""
import sys

n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

nums = set(nums)
nums = sorted(nums)

for i in nums:
    print(i)
