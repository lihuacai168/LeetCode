# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 15三数之和.py
# @Time : 2022/11/6 15:49
# @Email: lihuacai168@gmail.com


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) - 1

        nums.sort()
        ans = []

        target = 0
        # 固定第一个
        for first in range(n):

            # 第一个数前后相同时，去重
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            # 左右双指针
            right = n
            for left in range(first + 1, n):
                # 第二个数前后相同时，去重
                if left > first + 1 and nums[left] == nums[left - 1]:
                    continue

                while (
                    left < right and nums[first] + nums[left] + nums[right] > target
                ):
                    right -= 1

                # 退出上面循环时，有可能是second==third，两个相同，要去重
                # 也有可能是后面的表达式不成立
                if left == right:
                    break

                if nums[first] + nums[left] + nums[right] == target:
                    ans.append([nums[first], nums[left], nums[right]])

        return ans
