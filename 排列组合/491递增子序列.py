# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 491递增子序列.py
# @Time : 2022/11/7 19:12
# @Email: lihuacai168@gmail.com

# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
#
#  数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
#
#
#
#  示例 1：
#
#
# 输入：nums = [4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#
#
#  示例 2：
#
#
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 15
#  -100 <= nums[i] <= 100
#
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(nums: list[int], path: list, start_index: int):
            if len(path) >= 2:
                ans.append(path[:])

            level_set = set()
            for i in range(start_index, len(nums)):
                if path and nums[i] < path[-1]:
                    # 不符合递增的直接跳过
                    continue

                if nums[i] in level_set:
                    # 本层去重
                    continue
                path.append(nums[i])
                level_set.add(nums[i])
                backtracking(nums, path, i + 1)
                path.pop()

        backtracking(nums, [], 0)
        return ans


if __name__ == "__main__":
    s = Solution()
    s.findSubsequences([4, 6, 7, 7])
