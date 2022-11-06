# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 541反转字符串II.py
# @Time : 2022/11/6 16:10
# @Email: lihuacai168@gmail.com
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        left = 0
        right = len(s) - 1
        s_list = list(s)
        while left <= right:
            # 每隔2k个，前k个翻转
            # 当小于2k，大于k个时，前k个翻转
            if left + k <= right:
                # 翻转时，是包含了最后一位，当left=0, k=2如果没有减，是反转了k+1个字符
                reverse(s_list, left, left + k - 1)
            else:
                # 剩余小于k个时，全部翻转
                reverse(s_list, left, right)

            left += 2 * k
        # print(s_list)
        return "".join(s_list)
