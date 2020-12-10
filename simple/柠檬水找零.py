# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 柠檬水找零.py
# @Time : 2020/12/10 00:12
# @Email: lihuacai168@gmail.com
from typing import List


class Solution:
    """
    >>> s = Solution()
    >>> s.lemonadeChange([5,5,5,10,20])
    True

    >>> s.lemonadeChange([5,5,10])
    True

    >>> s.lemonadeChange([10, 10])
    False
    """
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}
        ans = True
        for i in bills:
            if i == 5:
                d[5] += 1
            elif i == 10:
                if d[5] < 1:
                    ans = False
                    break
                else:
                    d[5] -= 1
                    d[10] += 1
            else:
                if d[5] >= 1 and d[10] >= 1:
                    d[5] -= 1
                    d[10] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    ans = False
                    break
        return ans


class Solution1:
    """
    不需要使用哈希表来存储变量，直接使用单个变量即可
    >>> s = Solution1()
    >>> s.lemonadeChange([5,5,5,10,20])
    True

    >>> s.lemonadeChange([5,5,10])
    True

    >>> s.lemonadeChange([10, 10])
    False
    """
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five < 1:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
