# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 349两个数组的交集.py
# @Time : 2022/11/5 18:23
# @Email: lihuacai168@gmail.com


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        for num in nums1:
            m[num] = 1

        return [num for num in nums2 if m.get(num, 0)]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 直接调用系统函数就能解决问题时，这是不会被认可的
        return list(set(nums1).intersection(set(nums2)))
