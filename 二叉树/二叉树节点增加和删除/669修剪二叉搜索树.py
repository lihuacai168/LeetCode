# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional

# @Author: 花菜
# @File: 669修剪二叉搜索树.py
# @Time : 2022/11/2 15:50
# @Email: lihuacai168@gmail.com


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        # 左中右
        if not root:
            return

        if root.val < low:
            # 当节点值小于左区间时，不能直接返回，要递归调用
            # 右子树中可能存在符合要求的节点
            return self.trimBST(root.right, low, high)

        if root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root
