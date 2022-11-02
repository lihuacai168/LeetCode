# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional

# @Author: 花菜
# @File: 654最大二叉树.py
# @Time : 2022/11/2 17:25
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        # 找到数组中最大的元素root_val
        # 最大的元素构建root节点
        # 通过root_val切割数组，得到左右子树
        # 分别构建左右子树

        if not nums:
            return

        root_val = max(nums)
        root = TreeNode(root_val)
        if len(nums) == 1:
            return root

        sep_idx = nums.index(root_val)
        left_nums = nums[:sep_idx]
        right_nums = nums[sep_idx + 1 :]

        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)

        return root
