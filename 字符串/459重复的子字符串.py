# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 459重复的子字符串.py
# @Time : 2022/11/6 16:54
# @Email: lihuacai168@gmail.com


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        new_s = s + s
        i = 1
        # 如果一个字符串是由重复子串组成的
        # 这个重复子串拼接后，还能在新串的中间找到原来的子串
        # 为了避免重复，需要排除原来两个字符串
        # 所以需要从1开始遍历
        # 不需要等于n，因等于n证明前半部分遍历完了
        while i < n:
            if new_s[i: i + n] == s:
                return True
            i += 1
        return False
