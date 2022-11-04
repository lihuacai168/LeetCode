# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 704二分查找.py
# @Time : 2022/11/4 14:37
# @Email: lihuacai168@gmail.com


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 确定区间是左闭右闭
        # 所以right初始化为了len - 1
        left, right = 0, len(nums)-1

        # 因为区间是左闭右闭，所以left==right也是合法区间
        while left <= right:
            mid = (right+left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # 因为右区间是可以取到的，满足判断，证明mid一定是大于target，下次循环时，就可以排除mid
                right = mid - 1
            else:
                left = mid + 1

        return -1
