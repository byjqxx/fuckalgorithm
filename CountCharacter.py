class Solution:
    """
    计算某字符出现次数
    输入描述：第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。
    输出描述：输出输入字符串中含有该字符的个数。（不区分大小写字母）
    """
    str1 = input().lower()
    char1 = input().lower()
    nums = str1.count(char1)
    print(nums)


if __name__ == "__main__":
    test = Solution()
