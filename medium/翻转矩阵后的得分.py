# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 翻转矩阵后的得分.py
# @Time : 2020/12/7 12:58
# @Email: lihuacai168@gmail.com
"""
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

 

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/score-after-flipping-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    """
    >>> s = Solution()
    >>> s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
    39
    """

    def matrixScore(self, A):
        """
        先处理每行，保证第一个为1
        再处理列，使列中的1比0多
        :type A: List[List[int]]
        :rtype: int
        """
        for i, l in enumerate(A):
            if l[0] == 0:
                A[i] = [1 if j == 0 else 0 for j in l]
        row = len(A)
        col = len(A[0])

        # 按照列遍历
        for i in range(1, col):
            count = 0
            # 统计每列1的数量
            for j in range(row):
                count += A[j][i]
            # 每列的总数小于一半，证明0比1多，所以需要翻转
            if count < row / 2:
                for j in range(0, row):
                    if A[j][i] == 0:
                        A[j][i] = 1
                    else:
                        A[j][i] = 0

        return sum([int(''.join(map(str, i)), 2) for i in A])


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
