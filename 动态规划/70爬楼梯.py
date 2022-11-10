# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 70爬楼梯.py
# @Time : 2022/11/8 20:01
# @Email: lihuacai168@gmail.com
# 70爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#
#
#  示例 1：
#
#
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
#
#  示例 2：
#
#
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#
#
#
#
#  提示：
#
#
#  1 <= n <= 45
#
#
#  Related Topics 记忆化搜索 数学 动态规划 👍 2727 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# leetcode submit region end(Prohibit modification and deletion)
