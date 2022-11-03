# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 90子集II.py
# @Time : 2022/11/2 23:18
# @Email: lihuacai168@gmail.com


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 去重之前必须排序
        nums.sort()

        def backtracking(nums, used, start_index, path, paths):

            paths.append(path[:])

            for i in range(start_index, len(nums)):
                # used[i-1] is False，树层上去重，不能used[i-1] is True，这样是树枝上去重，会导致树枝上相同的元素取不到
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(nums, used, i + 1, path, paths)
                path.pop()
                used[i] = False

        paths = []
        used = [False for _ in range(len(nums))]
        backtracking(nums, used, 0, [], paths)
        return paths
