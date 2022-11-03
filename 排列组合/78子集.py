# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 78子集.py
# @Time : 2022/11/2 23:17
# @Email: lihuacai168@gmail.com


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, start_index, path, paths):
            # 收集结果
            # 所有结果都是符合要求，无需判断
            paths.append(path[:])

            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1, path, paths)
                # 回溯
                path.pop()

        paths = []
        backtracking(nums, 0, [], paths)
        return paths
