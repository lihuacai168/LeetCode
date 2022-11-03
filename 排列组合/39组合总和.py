# !/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import List

# @Author: 花菜
# @File: 39组合总和.py
# @Time : 2022/11/2 22:56
# @Email: lihuacai168@gmail.com


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def trackbacking(candidates, path, target, startIndex):
            if sum(path) > target:
                # 剪枝
                return

            if sum(path) == target:
                # 收集结果
                ans.append(path[:])
                return

            # 控制树层
            for i in range(startIndex, len(candidates)):
                path.append(candidates[i])
                # i不用+1，因为可以一个数可以重复使用,也就是树枝上取已经用过的值
                trackbacking(candidates, path, target, i)
                path.pop()  # 回溯

        trackbacking(candidates, path, target, 0)
        return ans
