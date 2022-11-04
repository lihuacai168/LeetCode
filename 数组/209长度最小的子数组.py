# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 209长度最小的子数组.py
# @Time : 2022/11/4 17:25
# @Email: lihuacai168@gmail.com


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, min_len = 0, 0, 0
        cur_sum = 0
        while right < len(nums):
            # cur_sum += nums[right]
            # 满足条件时，更新min_len
            # 删除左侧元素
            # 左指针+1
            # 右指针+1

            cur_sum += nums[right]
            while cur_sum >= target:
                if min_len == 0 or (right - left + 1) < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1
            right += 1

        return min_len
