# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 93复原IP地址.py
# @Time : 2022/11/6 19:07
# @Email: lihuacai168@gmail.com


class Solution:
    def __init__(self):
        self.result = []

    def is_valid(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False

        if s[start] == "0" and start != end:
            return False

        # 左闭右闭
        if not 0 <= int(s[start : end + 1]) <= 255:
            return False

        return True

    def backtracking(self, s: str, start_index: int, point_sum: int):
        if point_sum == 3:
            if self.is_valid(s, start_index, len(s)-1):
                self.result.append(s)
            return

        for i in range(start_index, len(s)):
            if self.is_valid(s, start_index, i):
                s = s[: i + 1] + "." + s[i + 1 :]
                point_sum += 1
                self.backtracking(s, i + 2, point_sum)
                point_sum -= 1
                s = s[: i + 1] + s[i + 2 :]
            else:
                break

    def restoreIpAddresses(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0, 0)
        return self.result
