# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional

# @Author: 花菜
# @File: 108将有序数组转换为二叉搜索树.py
# @Time : 2022/11/2 15:35
# @Email: lihuacai168@gmail.com

# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        if len(nums) == 1:
            return TreeNode(nums[0])

        idx = len(nums) // 2
        root = TreeNode(nums[idx])

        left_tree_nums = nums[:idx]
        right_tree_nums = nums[idx + 1 :]

        root.left = self.sortedArrayToBST(left_tree_nums)
        root.right = self.sortedArrayToBST(right_tree_nums)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def __sortedArrayToBST(left_idx, right_idx):
            if right_idx < left_idx:
                return

            mid = (left_idx + right_idx) // 2

            root = TreeNode(nums[mid])

            root.left = __sortedArrayToBST(left_idx, mid - 1)
            root.right = __sortedArrayToBST(mid + 1, right_idx)

            return root

        return __sortedArrayToBST(0, len(nums) - 1)
