# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 47全排列II.py
# @Time : 2022/11/2 23:13
# @Email: lihuacai168@gmail.com


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 排序是去重的提前
        nums.sort()

        def backtracking(nums, used, path, paths):
            if len(path) == len(nums):
                # 收获结果集
                paths.append(path[:])

            for i in range(len(nums)):
                # used[i-1] is False是同一层的剪枝，因为是同一层，i是从i-1回溯过去来的，i-1是没有被使用过的；
                # 同一层剪枝效果更好, 因为元素多时，一层下面还可能有很多的子树需要遍历
                # user[i-1] is True是树枝上的剪枝，i-1和i是在同一个树枝上
                if used[i] or (
                    i > 0 and nums[i] == nums[i - 1] and used[i - 1] is False
                ):
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(nums, used, path, paths)
                used[i] = False
                path.pop()

        paths = []
        used = [False for _ in range(len(nums))]
        backtracking(nums, used, [], paths)
        return paths
