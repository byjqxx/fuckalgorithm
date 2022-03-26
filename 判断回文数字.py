class Solution:
    """
    判断回文数字，如121
    %: 取余  12%10 = 2
    //: 取模 12//10 = 1

    方法一：将数字转换为字符串，然后反转字符串
    方法二：每次取余(y%10)，将余数放到新数(res)的最后一位
    """
    def ispalindrome1(self, n):
        return str(n)[::-1] == str(n)

    def ispalindrome2(self, x):
        if x < 0:
            return False
        res, y = 0, x
        while y != 0:
            res = res * 10 + y % 10
            y //= 10
        return res == x


s = Solution()
print(s.ispalindrome1(12121))
print(s.ispalindrome2(123454321))