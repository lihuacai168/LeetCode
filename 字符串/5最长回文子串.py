# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 5最长回文子串.py
# @Time : 2023/5/15 20:33
# @Email: lihuacai168@gmail.com

# 给你一个字符串
# s，找到
# s
# 中最长的回文子串。
#
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
#
#
#
# 示例
# 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba"
# 同样是符合题意的答案。

# 滑动窗口+动态规划dp
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 中心扩展法
        # 传输两个指针，一个往左，一个往右，找到最大的回文，返回

        start, end = 0, 0
        n = len(s)

        for i in range(n):
            left1, right1 = self.mid(s, i, i)
            left2, right2 = self.mid(s, i, i + 1)

            # 实际长度是要+1，因为两边都+1，直接省略
            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2

        # 取值是到end
        return s[start : end + 1]

    def mid(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        """
        这是因为在这个 `while` 循环中，当 `left >= 0` 和 `right < len(s)` 以及 `s[left] == s[right]` 的条件不再满足时，循环才会终止。这可能是因为 `left` 小于 `0`，或者 `right` 大于或等于 `len(s)`，或者 `s[left]` 不等于 `s[right]`。
在任何一种情况下，`left` 和 `right` 的当前值都不在回文串的范围内。如果是 `left` 小于 `0` 或者 `right` 大于或等于 `len(s)`，那么这个索引超出了字符串的范围。如果是 `s[left]` 不等于 `s[right]`，那么这两个字符不能同时出现在回文串中。
因此，我们返回 `left+1` 和 `right-1`，而不是 `left` 和 `right`。这样返回的就是回文串的正确的左右边界。
        """
        return left + 1, right - 1


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp
        # 初始化dp数组，dp[i][j]表示s[i:j+1]是回文
        # 转移方程dp[i][j] = (dp[i+1][j-1] and s[i]==s[j])
        n = len(s)
        dp = [[False] * n for i in range(n)]
        max_sub = ""

        for l in range(len(s)):
            for i in range(len(s)):
                j = i + l
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                if dp[i][j] and (j - i + 1) > len(max_sub):
                    max_sub = s[i : j + 1]

        return max_sub


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp
        # 初始化dp数组，dp[Flase] * n
        n = len(s)
        if n < 2:
            return s

        dp = [False] * n
        max_len = 1
        start = 0

        for j in range(1, n):
            new_dp = dp[:]
            for i in range(0, j):
                # 在这个算法中，我们其实是从左向右遍历字符串的，但是在考虑每个子串是否为回文串时，我们是从一个较大的子串开始，逐渐减小到较小的子串。
                # 这就是我所说的“从右向左（从大索引向小索引）”。
                # 具体来说，我们首先固定右端点 j，然后从 j 向左遍历到 i。在每次迭代中，我们都检查从 i 到 j 的子串是否为回文。
                # 这就意味着我们先检查了较大的子串（当 i 接近 0 时），然后逐渐检查较小的子串（当 i 接近 j 时）。这就是我所说的“从右向左（从大索引向小索引）”。
                if s[i] == s[j]:
                    if j - i < 3:
                        new_dp[i] = True

                    else:
                        new_dp[i] = dp[i + 1]
                else:
                    new_dp[i] = False

                if new_dp[i] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i

            dp = new_dp
        return s[start : start + max_len]
