# -*- encoding:utf-8 -*-
from collections import defaultdict


class Solution():
    """
    统计列表中重复项的出现次数
    """
    def count_item(self, alist):
        d = defaultdict(int)
        for item in alist:
            d[item] += 1
        return dict(d)

class Solution2():
    def count_item(self, alist):
        d = {}
        s = set(alist)
        for i in s:
            d[i] = alist.count(i)
        return d


str1 = 'dadsdfdsdfsaas'
list1 = [1, 2, 3, 1, 2, 3, 1]
s1 = Solution()
s2 = Solution2()
d1 = s1.count_item(str1)
d2 = s2.count_item(list1)
print(d1)
print(d2)