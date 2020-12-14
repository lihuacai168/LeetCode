# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 最大子序和.py
# @Time : 2020/12/14 13:04
# @Email: lihuacai168@gmail.com

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    """
    >>> s = Solution()
    >>> s.maxSubArray([1,-1,1])
    1
    >>> s.maxSubArray([8,-19,5,-4,20])
    21
    >>> s.maxSubArray([-2,1])
    1
    >>> s.maxSubArray([-1])
    -1
    >>> s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    6

    >>> s.maxSubArray([1,2])
    3
    """


    def maxSubArray(self, nums):
        maxValue = nums[0]
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] + nums[i - 1] > nums[i]:
                nums[i] += nums[i - 1]

            if nums[i] > maxValue:
                maxValue = nums[i]
            i += 1
        return maxValue


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
