# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 3无重复字符的最长子串.py
# @Time : 2023/5/15 10:49
# @Email: lihuacai168@gmail.com
# 给定一个字符串
# s ，请你找出其中不含有重复字符的
# 最长子串
# 的长度。
#
#
#
# 示例
# 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是
# "abc"，所以其长度为
# 3。
# 示例
# 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是
# "b"，所以其长度为
# 1。
# 示例
# 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是
# "wke"，所以其长度为
# 3。
# 请注意，你的答案必须是
# 子串
# 的长度，"pwke"
# 是一个子序列，不是子串。

# 滑动窗口

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 双指针
        # 左边固定，右边移动
        # 右边移动
        # 判断右边+1，是否在子串中
        # 不在，右边移动，更新最大子串长度
        # 在， 左边+1，《 右边，直到符合不重复子串
        n = len(s)
        if n <= 1:
            return n

        left, right = 0, 1
        window = set()
        window.add(s[left])
        max_len = len(window)
        while right < n:
            if s[right] not in window:
                window.add(s[right])
                right += 1
                max_len = max(len(window), max_len)
            else:
                while left < right and s[right] in window:
                    left += 1
                    window = set(s[left:right])
        return max_len


class Solution:
    # gpt4
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        left, right = 0, 0
        window = set()
        max_len = 0

        while right < n:
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            right += 1
            max_len = max(right - left, max_len)
        return max_len
