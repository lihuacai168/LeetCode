# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 杨辉三角.py
# @Time : 2020/12/6 00:51
# @Email: lihuacai168@gmail.com

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> s.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        True

        >>> s.generate(1) == [[1]]
        True

        >>> s.generate(0) == []
        True
        """
        if numRows == 0:
            return []

        ans = [[1]]
        i = 0
        while i < numRows - 1:
            t = []
            l = [0] + ans[i] + [0]
            for j in range(len(l) - 1):
                t.append(l[j] + l[j + 1])
            ans.append(t)
            i += 1
        return ans


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
