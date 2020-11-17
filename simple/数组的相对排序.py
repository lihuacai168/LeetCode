# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 数组的相对排序.py
# @Time : 2020/11/17 23:32
# @Email: lihuacai168@gmail.com
"""
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在arr1中
对 arr1中的元素进行排序，使 arr1 中项的相对顺序和arr2中的相对顺序相同。未在arr2中出现过的元素需要按照升序放在arr1的末尾。



示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]


提示：

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2中的元素arr2[i]各不相同
arr2 中的每个元素arr2[i]都出现在arr1中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def relativeSortArray(self , arr1 , arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        import collections
        import itertools

        count = dict(collections.Counter(arr1))

        item_in_arr1 = list(itertools.chain.from_iterable([count.pop(i) * [i] for i in arr2 if i in count.keys()]))

        item_not_in_arr1 = list(itertools.chain.from_iterable([v * [k] for k , v in count.items()]))
        item_not_in_arr1.sort()
        return item_in_arr1 + item_not_in_arr1