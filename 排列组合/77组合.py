# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 77组合.py
# @Time : 2022/11/2 23:02
# @Email: lihuacai168@gmail.com


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def trackbacking(n, k, start_index):
            if len(path) == k:
                # 需要把path复制进去，不然保存的是引用
                res.append(path[:])
                return

            # for i in range(start_index, n+1):
            # 剪枝
            # 最多的起始位置是n - (k - len(path)) + 1
            # +1 是因为start_index从1开始
            # 要包含最后一项，因此需要再+1
            for i in range(start_index, n - (k - len(path)) + 1 + 1):
                path.append(i)
                # 注意不能用start_index + 1，因为这个不会改变，用i+1来控制
                trackbacking(n, k, i + 1)
                path.pop()

        trackbacking(n, k, 1)
        return res
