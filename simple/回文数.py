# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 回文数.py
# @Time : 2020/12/7 22:47
# @Email: lihuacai168@gmail.com
class Solution:
    """
    >>> s = Solution()
    >>> s.isPalindrome(121)
    True

    >>> s.isPalindrome(-121)
    False

    >>> s.isPalindrome(10)
    False

    >>> s.isPalindrome(0)
    True
    """

    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x > 0:
            s = str(x)
            return s == s.lstrip('0')[::-1]
        else:
            return False


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
