# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Optional

# @Author: 花菜
# @File: 700二叉搜索树中的搜索.py
# @Time : 2022/11/2 17:21
# @Email: lihuacai168@gmail.com


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == val:
            return root

        ans = None
        if val < root.val:
            ans = self.searchBST(root.left, val)
        if val > root.val:
            ans = self.searchBST(root.right, val)

        return ans
