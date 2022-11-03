# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 784字母大小写全排列.py
# @Time : 2022/11/3 07:52
# @Email: lihuacai168@gmail.com


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        chars = [ch for ch in s]
        n = len(chars)

        def backtracking(chars, index, n):
            nonlocal paths
            paths.append("".join(chars))
            for i in range(index, n):
                if chars[i].isdigit():
                    continue

                chars[i] = chars[i].swapcase()  # 大小写转换
                backtracking(chars, i + 1, n)
                chars[i] = chars[i].swapcase()  # 回溯，恢复原来的字符

        paths = []
        backtracking(chars, 0, n)
        return paths


s = Solution()
s.letterCasePermutation("a1b2")
