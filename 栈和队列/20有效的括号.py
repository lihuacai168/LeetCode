# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 20有效的括号.py
# @Time : 2022/11/6 17:56
# @Email: lihuacai168@gmail.com


class Solution:
    def isValid(self, s: str) -> bool:
        m = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                # ) ] }
                if not stack:
                    return False
                #
                out = stack.pop()
                if m[c] != out:
                    return False
        if stack:
            return False
        return True
