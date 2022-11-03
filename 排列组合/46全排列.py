# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 46全排列.py
# @Time : 2022/11/2 23:09
# @Email: lihuacai168@gmail.com


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, used, path, paths):
            if len(path) == len(nums):
                # 收获结果集
                paths.append(path[:])

            # 排序的元素是有序的，取值应该是每次都从头开始
            # 然后通过used来排除已经使用过的元素
            for i in range(len(nums)):
                if used[i]:
                    # 去重
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(nums, used, path, paths)
                # 回溯
                used[i] = False
                path.pop()

        paths = []
        # 排列时，需要记录已经使用过的元素
        used = [False for _ in range(len(nums))]
        backtracking(nums, used, [], paths)
        return paths
