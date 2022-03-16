# -*- encoding:utf-8 -*-

class Solution:
    """
    给定两个字符串 s 和 t，判断它们是否是同构的。
    如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
    所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

    如：
        输入: s = “egg”, t = “add”
        输出: true
        输入: s = “foo”, t = “bar”
        输出: false
        输入: s = “paper”, t = “title”
        输出: true

    条件：
        1 <= s.length <= 5 * 10^4
        t.length == s.length
        s 和 t 由任意有效的 ASCII 字符组成
    """
    def isIsomorphic(self, s, t):
        # d = dict([(i, s[i]) for i in range(len(s))])
        for i in range(len(s)):
            # 判断字符串s中的字符是否在之前遍历过的部分出现过
            # 如果出现过，字符串t相同位置的字符也应该相同，否则不是同构
            if s[i] in s[:i]:
                if t[s[:i].index(s[i])] != t[i]:
                    return False
            else:
                # 如果字符串t中的某个字符在之前遍历过的部分出现过
                # 而在字符串s中，这个位置的字符之前没有出现过，说明不是同构
                if t[i] in t[:i]:
                    return False
        return True


class Solution2:
    def isIsomorphic(self, s, t):
        return len(set(s)) == len(set(t)) and len(set(s)) == len(set(zip(s, t)))



s = Solution2()
print(s.isIsomorphic('add', 'egg'))
print(s.isIsomorphic('paper', 'title'))
print(s.isIsomorphic('foo', 'bar'))
print(s.isIsomorphic('test', 'hehe'))
print(s.isIsomorphic('Hello', 'abcce'))
print(s.isIsomorphic('abdde', 'qwert'))