# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 不同路径.py
# @Time : 2020/12/9 23:11
# @Email: lihuacai168@gmail.com
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    >>> s = Solution()
    >>> s.uniquePaths(7, 3)
    28

    >>> s.uniquePaths(3, 2)
    3
    """

    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划
        # 先创建一个m * n的矩阵
        # 矩阵的第一个元素全部设置为[1, 1, 1]
        # 其他的m-1个元素设置[1, 0, 0], 默认横坐标都是1，因为答案就是这么说的，嘻嘻~
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
