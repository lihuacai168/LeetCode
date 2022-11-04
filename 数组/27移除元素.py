# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 27移除元素.py
# @Time : 2022/11/4 15:47
# @Email: lihuacai168@gmail.com

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                # 如果right的值刚好等于val
                # 下一次循环，left没变，所以还会继续覆盖
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left

    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针复制
        # 快指针先走，遇到不等于val时，就把值复制到slow，复制完，slow+1
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
