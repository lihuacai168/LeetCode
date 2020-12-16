# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 单词规律.py
# @Time : 2020/12/16 01:21
# @Email: lihuacai168@gmail.com

class Solution:
    """
    >>> s = Solution()
    >>> s.wordPattern("abba", "dog cat cat dog") is True
    True

    >>> s.wordPattern("abc", "b c a")
    True
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d1 = {}
        n = len(pattern)
        words = s.split(" ")
        if len(words) != n:
            return False

        for i in range(n):
            if d.get(pattern[i]):
                d[pattern[i]] += i
            else:
                d[pattern[i]] = i

            if d1.get(words[i]):
                d1[words[i]] += i
            else:
                d1[words[i]] = i

        for i in range(n):
            if d[pattern[i]] != d1[words[i]]:
                return False

        return True


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
