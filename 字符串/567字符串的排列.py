# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 567字符串的排列.py
# @Time : 2023/5/17 15:40
# @Email: lihuacai168@gmail.com

#
# 给你两个字符串
# s1
# 和
# s2 ，写一个函数来判断
# s2
# 是否包含
# s1
# 的排列。如果是，返回
# true ；否则，返回
# false 。
#
# 换句话说，s1
# 的排列之一是
# s2
# 的
# 子串 。
#
#
#
# 示例
# 1：
#
# 输入：s1 = "ab"
# s2 = "eidbaooo"
# 输出：true
# 解释：s2
# 包含
# s1
# 的排列之一("ba").
# 示例
# 2：
#
# 输入：s1 = "ab"
# s2 = "eidboaoo"
# 输出：false
#
# 提示：
#
# 1 <= s1.length, s2.length <= 104
# s1
# 和
# s2
# 仅包含小写字母

# 滑动窗口

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        window_counter = Counter()

        # 窗口一直往右滑动
        # 当窗口长度大于等于s1长度
        # 判断最左侧的元素是否符合应该被剔除
        # 只剩下一个时，直接删除；大于1，就减1
        for i, char in enumerate(s2):
            window_counter[char] += 1

            if i >= len(s1):
                # 找到窗口最左侧的元素索引
                if window_counter[s2[i - len(s1)]] == 1:
                    del window_counter[s2[i - len(s1)]]
                else:
                    window_counter[s2[i - len(s1)]] -= 1

            if window_counter == s1_counter:
                return True

        return False