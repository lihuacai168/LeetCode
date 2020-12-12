# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 存在重复元素.py
# @Time : 2020/12/13 01:22
# @Email: lihuacai168@gmail.com
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if d.get(i, 0) > 0:
                return True
            else:
                d[i] = 1
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        if len(set(nums)) < len(nums):
            return True
        else:
            return False
