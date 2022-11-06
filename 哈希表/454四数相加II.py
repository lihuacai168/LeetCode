# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 454四数相加II.py
# @Time : 2022/11/6 15:42
# @Email: lihuacai168@gmail.com
class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        m = {}
        ans = 0
        for i in nums1:
            for j in nums2:
                # 统计两个数相加频率
                m[i + j] = m.get(i + j, 0) + 1

        for k in nums3:
            for j in nums4:
                find = 0 - (k + j)
                if find in m:
                    ans += m[find]
        return ans
