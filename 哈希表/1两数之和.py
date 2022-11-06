# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 1两数之和.py
# @Time : 2022/11/5 18:38
# @Email: lihuacai168@gmail.com


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 遍历数组的下标和元素
        # 如果找到符合目标值，直接返回
        # 找不到就把当前元素作为key，下标作为value保存到map
        m = {}
        for idx, num in enumerate(nums):
            find = target - num
            if find in m:
                return [idx, m[find]]
            else:
                m[num] = idx
