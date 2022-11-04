# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 977有序数组的平方.py
# @Time : 2022/11/4 17:20
# @Email: lihuacai168@gmail.com


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = []
        # 当left==right时，还需要做处理，否则就会漏掉这个元素
        while left <= right:
            if pow(nums[left], 2) > pow(nums[right], 2):
                ans.append(pow(nums[left], 2))
                left += 1
            else:
                ans.append(pow(nums[right], 2))
                right -= 1

        return ans[::-1]
