# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 131分割回文串.py
# @Time : 2022/11/6 18:56
# @Email: lihuacai168@gmail.com


class Solution:
    def is_palindrome(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def backtracking(s, start_index):
            if start_index == len(s):
                ans.append(path[:])

            for i in range(start_index, len(s)):
                if self.is_palindrome(s, start_index, i):
                    # 截取子串时，是开区间，要包含i，所以需要i+1
                    path.append(s[start_index: i + 1])
                else:
                    continue
                backtracking(s, i + 1)
                path.pop()

        backtracking(s, 0)
        return ans
