# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 三角形的最大周长.py
# @Time : 2020/11/29 20:28
# @Email: lihuacai168@gmail.com
class Solution(object):
    """
    >>> s = Solution()
    >>> s.largestPerimeter([2,1,2]) == 5
    True

    """
    # 倒叙遍历
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        ans = 0
        A.sort()
        j = n - 3
        while j >= 0:
            l = A[j:j + 3]
            if len(l) < 3:
                break
            if self.is_angle(l):
                ans = sum(l)
                break
            j -= 1
        return ans

    # 顺序遍历
    def largestPerimeter(self, A):

        n = len(A)
        if n < 3:
            return 0
        ans = 0
        A.sort(reverse=True)
        i = 0
        while i <= n - 3:
            l = A[i:i+3]
            if len(l) < 3:
                break
            if self.is_angle(l):
                ans = sum(l)
                break
            i += 1
        return ans

    def is_angle(self, l):
        if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[2] + l[0] > l[1]:
            return True
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
