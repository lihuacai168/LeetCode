# !/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import Counter

# @Author: 花菜
# @File: 424替换后的最长重复字符.py
# @Time : 2023/5/17 17:02
# @Email: lihuacai168@gmail.com


# 给你一个字符串
# s
# 和一个整数
# k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行
# k
# 次。
#
# 在执行上述操作后，返回包含相同字母的最长子字符串的长度。
#
#
#
# 示例
# 1：
#
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个
# 'A'
# 替换为两个
# 'B', 反之亦然。
# 示例
# 2：
#
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个
# 'A'
# 替换为
# 'B', 字符串变为
# "AABBBBA"。
# 子串
# "BBBB"
# 有最长重复字母, 答案为
# 4。
# 可能存在其他的方法来得到同样的结果。


# 滑动窗口


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # 设置左右指针为窗口的两边
        # 右边指针开始滑动
        # 把元素加入到窗口
        # 更新最长的重复长度
        # 如果统计窗口内，除了最多的元素外，其他元素个数大于k时，移除窗口最左侧的元素

        window = []
        left, right = 0, 0
        max_repeat = 1
        while right < len(s):
            window.append(s[right])
            # 会超时
            c = Counter(window)
            if len(c.keys()) > 1 and c.most_common(1):
                if len(window) - c.most_common(1)[0][1] > k:
                    window.pop(0)
            max_repeat = max(max_repeat, len(window))
            right += 1
        return max_repeat


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # 设置左右指针为窗口的两边
        # 右边指针开始滑动
        # 把元素加入到窗口
        # 更新最长的重复长度
        # 如果统计窗口内，除了最多的元素外，其他元素个数大于k时，移除窗口最左侧的元素
        count = [0] * 26  # 另类窗口
        left = right = 0
        max_count = 0
        mex_len = 0
        while right < len(s):
            count[ord(s[right]) - ord("A")] += 1
            max_count = max(max_count, count[ord(s[right]) - ord("A")])

            if right - left + 1 > max_count + k:
                # 窗口左侧移除
                count[ord(s[left]) - ord("A")] -= 1
                left += 1
            max_len = max(mex_len, right - left + 1)
            right += 1
        return max_len
