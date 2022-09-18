# -*- coding:utf-8 -*-

class BubbleSort:
    """
    冒泡排序,升序
    """
    def bubbleSort(self, s):
        for i in range(len(s)):
            # i 从0开始，每循环完 1 次，找出来了 1 个最大值
            # 所以下次循环只需要完成列表前 len(s)-i 个元素的排序
            # 即，将前len(s)-i个元素中的第一个元素依次与前len(s)-i个元素中的每个元素比较
            # 由于前 len(s)-i 个元素，j 每次循环到倒数第二个，即 倒数第二个与最后一个元素比较
            # 所以每次循环中,j 的最后一个取值为倒数第二个元素下标，就完成了一次排序
            # 前 len(s)-i 个元素的长度是 len(s)-i，
            # 第一个元素到倒数第二个元素的下标范围是 range(len(s)-i-1)
            # 所以 j 的取值范围是 range(len(s)-i-1)
            for j in range(len(s)-i-1):
                # j每次循环都从0开始，即用第一个元素依次和后面的元素比较
                # 每次交换，将这次循环找到的最大的值交换到后面
                if s[j] > s[j+1]:
                    s[j+1], s[j] = s[j], s[j+1]
        return s

    def bubbleSort2(self, s):
        for i in range(len(s)):
            # i 每 循环完一次，找到一个最小值，并将最小值交换到列表第一个位置
            # 所以下次循环从第 i+1 个元素元素开始，一直比较到列表最后一个元素
            # 所以 j 的循环范围是 range(i+1, len(s))
            for j in range(i+1, len(s)):
                # 每次交换，将这次循环找到的最小的值交换到前面
                if s[j] < s[i]:
                    s[i], s[j] = s[j], s[i]
        return s


b = BubbleSort()
l1 = b.bubbleSort([2, 5, 100, 8, 3, 9, 23, 54, 12, 1, 7, 8])
l2 = b.bubbleSort2([100, 54, 23, 12, 45, 19, 18, 28, 17, 5, 33, 2, 1])
print(l1)
print(l2)
