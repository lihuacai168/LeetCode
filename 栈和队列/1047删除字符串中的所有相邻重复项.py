# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 1047删除字符串中的所有相邻重复项.py
# @Time : 2022/11/6 17:57
# @Email: lihuacai168@gmail.com


class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        for ch in s:
            # stack[-1]之前，需要判断stack是否为空
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
