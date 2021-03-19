# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 数组中重复的数据.py
# @Time : 2021/3/19 10:29
# @Email: lihuacai168@gmail.com

"""
找数组中重复数据
给定一个整数数组a,其中1≤a(1)≤n(n为数组长度）,其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
不用到任何额外空间并在O(n)时间复杂度内解决这个问题
示例：
输入：[4,3,2,7,8,2,3,1]
输出：[2,3]
"""


from typing import List


class Solution:
    """
    >>> s = Solution()
    >>> s.findDuplicates([4, 3, 2, 7, 8, 7, 3, 1])
    [7, 3]
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        rst = []
        for num in nums:
            # 因为我们是直接原地修改元素为负值来标记是否访问过，因此这里的num一定要取绝对值
            index = abs(num) - 1
            val = nums[index]
            if val < 0:
                # 如果元素值为负数，说明之前存在同一个索引为num的元素
                rst.append(abs(num))
            # 原地修改访问标志
            nums[index] = -nums[index]
        return rst


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
