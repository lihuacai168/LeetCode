# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 347前K个高频元素.py
# @Time : 2022/11/6 18:10
# @Email: lihuacai168@gmail.com


import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        # 先统计每个元素出现的次数
        # 再把次数和元素加入到小顶堆，按照次数排序
        # 当堆的长度大于k时，就把堆顶的元素剔除掉，也就是说剩余的都是比堆顶要大
        for key, freq in Counter(nums).items():
            heapq.heappush(heap, (freq, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [tp[1] for tp in heap]
