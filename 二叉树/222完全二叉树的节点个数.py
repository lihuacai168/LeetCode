# !/usr/bin/python3
# -*- coding: utf-8 -*-

from typing import List, Optional


# @Author: 花菜
# @File: 222完全二叉树的节点个数.py
# @Time : 2022/11/2 17:33
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)

        return leftCount + rightCount + 1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # 判断节点的左右子树是不是满二叉树
        # 条件是左右子树的深度相等
        leftNode = root.left
        rightNode = root.right

        leftDepth = 1
        rightDepth = 1

        while leftNode:
            leftDepth += 1
            leftNode = leftNode.left

        while rightNode:
            rightDepth += 1
            rightNode = rightNode.right

        if leftDepth == rightDepth:
            # 满二叉树节点数量计算公式
            # 2的深度次方
            return pow(2, leftDepth) - 1

        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)

        return leftCount + rightCount + 1
