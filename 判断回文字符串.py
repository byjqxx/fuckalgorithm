class Solution:
    """
    判断回文字符串
    方法一：切片
    方法二：reversed() 函数 接受一个元素序列并返回该序列的反向迭代器。
    """
    def isPalindrome1(self, s):
        return s[::-1] == s

    def isPalindrome2(self, s:str):
        return s == "".join(reversed(s))


s = Solution()
print(s.isPalindrome1("abcba"))
print(s.isPalindrome2("aaa"))