# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 151反转字符串中的单词.py
# @Time : 2022/11/6 16:33
# @Email: lihuacai168@gmail.com


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        s = s.strip()
        res = ""
        slow = fast = 0
        while fast < len(s):
            # 如果快指针遇到空格
            # 1.快慢指针之间是单词
            # 2.快慢指针是空格
            if s[fast] == " ":
                if s[slow:fast] != " ":
                    res = s[slow:fast].strip() + " " + res
                slow = fast
            fast += 1
        res = s[slow:fast].strip() + " " + res
        return res.strip()
