# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 343整数拆分.py
# @Time : 2022/11/9 19:04
# @Email: lihuacai168@gmail.com
# 343整数拆分
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
#
#  返回 你可以获得的最大乘积 。
#
#
#
#  示例 1:
#
#
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
#
##  示例 2:
#
#
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
#
#
#
#  提示:
#
#
#  2 <= n <= 58
#
#
#  Related Topics 数学 动态规划 👍 971 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i]数组表示整数i可以拆分的最大乘积
        # 当i>2时，对于正整数i可以拆分出来第一个正整数j(1<=j<i),则有一下方案
        # 1、将i拆分成j和i-j，并且i-j不再拆分，此时的乘积是j*(i-j)
        # 2、将i拆分成j和i-j, 且i-j继续拆分，此时的乘积是j*dp[i-j]
        # 所以状态转移方程有 dp[i] = max(j*(i-j), j*dp[i-j])
        # j的范围是i-1

        dp = [0 for _ in range(n + 1)]
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                # 在循环过程中，i是固定的，所以需要跟每次计算的值对比，取最大值
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]


# leetcode submit region end(Prohibit modification and deletion)
