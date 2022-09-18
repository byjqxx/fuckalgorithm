# -*- encoding:utf-8 -*-

class Solution():
    """
    题目：
        字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
        比如，字符串 aabcccccaaa 会变为 a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。
        你可以假设字符串中只包含大小写英文字母（a至z）。
    示例：
        输入："aabcccccaaa"
        输出："a2b1c5a3"
        
        输入："abbccd"
        输出："abbccd"
        解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

    提示：
        字符串长度在[0, 50000]范围内。
    
    思路：
    初始值：
        p = 0  -> 比较的基准
        i = 1  -> 循环控制
        c = 1  -> 字符重复次数
    情况：
    #当 i 移动到列表最后一位时，循环结束，不再进行下次循环
    while i <= len(s)-1:
        #当 p 移动到最后一位时，循环结束
        #判断重复次数 c 是否大于1
        # 如果大于 1 ，将 c 添加到列表最后
        # 将 c 转换为字符串，然后将每个字符添加到列表s末尾
        if p >= len(s)-1:
            if c > 1:
                for j in str(c):
                    s.append(j)
                    break
            else
                return s
        else:
            #当 p 和 i 处的值不等时，都向后移动一位
            if s[i] != s[p]:
                p += 1
                i += 1
            #当 p 和 i 处的值相等时，移除i处的数，p的重复数c加1
            else:
                s.pop(i)
                c += 1
                # 每次比较完，不一定有下一次循环
                # 所以比较之后，判断是否将 c 插入字符串中
                if s[p] != s[i]:
                    # 将 c 的每一位一次插入字符串中
                    for j in str(c):
                        s.insert(i, j)
                    # 插入之后，p的位置和i的位置都要移动
                    p = p + len(str(c)) + 1
                    i = p + 1
                # 如果p和i相同的话，暂时不插入c，p不变，i也不变
                else:
                    continue
                    
    """
def compress(s):
    p = 0
    c = 1
    while True:
        # p 的值不超过列表最后一个值的下标时
        if p < len(s)-1:
            # p 处的值与 p+1 处的值不相等
            if s[p] != s[p+1]:
                # 判断上次循环完后，p处的重复次数c是否大于1
                # 如果大于1，插入p处值的次数，然后将c重置为1
                if c > 1:
                    # 先将 c 转化为字符串
                    # 如果 c 超过两位，比如 21
                    # 在 p+1 前分别插入这两个数字的话，
                    # 21 会变成 12
                    # 所以将字符串先倒转一下
                    # 插入后才能恢复正确顺序
                    for j in str(c)[::-1]:
                        print(j)
                        s.insert(p+1, j)
                    p = p + len(str(c)) + 1
                    c = 1
                # 如果 p 的重复次数不超过1，则继续移动p，继续开始下次循环
                else:
                    p += 1
                    continue
            else:
                # 如果 p 处与 p+1 处的值相等，则移除 p+1 处元素，c 加 1 
                s.pop(p+1)
                c += 1
        # p 为列表最后一个值时
        elif p == len(s) - 1:
            if c > 1:
                for j in str(c):
                    s.append(j)
            break
    return s

# s1 = list("aaabbbbbbbbbbbbbbbb")
# s1 = ["a"]
# s1 = ["a", "a"]
# s1 = ["a", "b"]
# s1 = ["a", "b", "b", "b"]
s1 = ["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]
s2 = compress(s1)
print(s2)