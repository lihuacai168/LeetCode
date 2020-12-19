# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 旋转图像.py
# @Time : 2020/12/19 01:17
# @Email: lihuacai168@gmail.com
from typing import List


class Solution:
    """
    >>> s = Solution()
    >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
    >>> s.rotate(matrix)
    >>> matrix
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 上下翻转
        for i in range(n//2):
            matrix[i], matrix[n-1 - i] = matrix[n - 1 - i], matrix[i]

        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                # print(matrix)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
