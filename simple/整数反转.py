# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 整数反转.py
# @Time : 2020/12/7 22:18
# @Email: lihuacai168@gmail.com

class Solution(object):
    """
    >>> s = Solution()
    >>> s.reverse(1534236469)
    0
    >>> s.reverse(123)
    321
    >>> s.reverse(120)
    21
    >>> s.reverse(-123)
    -321

    >>> s.reverse(0)
    0

    >>> s.reverse(-1230)
    -321


    """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if x == 0:
            return ans

        s = str(x)
        if x > 0:
            s = s[::-1]
            ans = int(s.lstrip('0'))

        else:
            s = s.replace('-', '')[::-1]
            ans = -int(s.lstrip('0'))
        MAX = 2**31 - 1
        MIN = -2 ** 31
        if MIN > ans or ans > MAX:
            ans = 0
        return ans


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
