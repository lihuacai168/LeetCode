# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 62不同路径.py
# @Time : 2022/11/8 22:38
# @Email: lihuacai168@gmail.com
# 62不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
#  问总共有多少条不同的路径？
#
#
#
#  示例 1：
#
#
# 输入：m = 3, n = 7
# 输出：28
#
#  示例 2：
#
#
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
#
#
#  示例 3：
#
#
# 输入：m = 7, n = 3
# 输出：28
#
#
#  示例 4：
#
#
# 输入：m = 3, n = 3
# 输出：6
#
#
#
#  提示：
#
#
#  1 <= m, n <= 100
#  题目数据保证答案小于等于 2 * 10⁹
#
#
#  Related Topics 数学 动态规划 组合数学 👍 1603 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 递推公式，因为机器人只能向前或者向下
        # dp[i][j]只能是从d[i-1][j](左边)和d[i][j-1]上面来
        # 所以dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # dp数组的意思，表示从(0,0)到(i,j)有d[i][j]条不同的路径
        # dp数组初始化横向d[0][0] - d[i-1][0]
        # dp数组初始化纵向d[0][0] - d[0][j-1]
        # 遍历顺序，从前到后
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # 遍历需要从1开始，因为0的位置算是初始化的
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # 从0开始，左闭右开
        return dp[m - 1][n - 1]


# leetcode submit region end(Prohibit modification and deletion)
