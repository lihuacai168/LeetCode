# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List

# @Author: 花菜
# @File: 215数组中的第K个最大元素.py
# @Time : 2022/11/3 08:24
# @Email: lihuacai168@gmail.com

# topK快排模板
# https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/821137/ji-yu-kuai-pai-de-suo-you-topkwen-ti-jia-ylsd/?languageTags=python3


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr, left, right):
            pivot = arr[left]
            while left < right:
                while left < right and arr[right] >= pivot:
                    # 从右往左遍历，找到第一个比privot小的数
                    right -= 1
                # 可以覆盖arr[left]，因为已经被pivot保存起来这个值
                arr[left] = arr[right]

                while left < right and arr[left] <= pivot:
                    # 从左到右遍历，找到第一个比pivot到数
                    left += 1
                # 然后把这个数放在pivot的右边
                # 上面right停止的位置，这个已经放到了arr[left]，这里可以直接覆盖
                arr[right] = arr[left]
            arr[left] = pivot
            # 退出时，left之前的都数都小于pivot
            # len(arr) - left 的数都大于pivot
            return left

        def topk_split(nums, k, left, right):
            if left < right:
                index = partition(nums, left, right)
                if index == k:
                    return
                elif index < k:
                    # index的位置，还没有达到k个最小， index右边还需要在排序
                    topk_split(nums, k, index + 1, right)

                else:
                    topk_split(nums, k, left, index - 1)

        # 前k个最大，也就相当于len(nums)-k个最小
        topk_split(nums, len(nums) - k, 0, len(nums) - 1)

        return nums[len(nums) - k]


s = Solution()
s.findKthLargest([3, 2, 3, 4, 5, 5, 6, 1, 2], 4)
