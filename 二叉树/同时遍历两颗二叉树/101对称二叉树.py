# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Optional


# @Author: 花菜
# @File: 101对称二叉树.py
# @Time : 2022/11/2 17:52
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def compare(left, right) -> bool:
            # 枚举左右子树为空和不为空
            # 比较左右子树的值相等和不相等于
            if left is None and right is not None:
                return False

            elif left is not None and right is None:
                return False

            elif left is None and right is None:
                return True

            elif left.val != right.val:
                return False

            # 到这里，证明左右子树都不为空，并且val相等，
            # 需要进行下一层递归，比较左右子树的内侧和外侧

            # 比较当前节点的外侧
            outside = compare(left.left, right.right)
            # 比较当前节点的内侧
            inside = compare(left.right, right.left)
            return outside and inside

        return compare(root.left, root.right)
