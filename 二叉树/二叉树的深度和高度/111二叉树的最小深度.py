# !/usr/bin/python3
# -*- coding: utf-8 -*-

import collections
# @Author: 花菜
# @File: 111二叉树的最小深度.py
# @Time : 2022/11/2 17:36
# @Email: lihuacai168@gmail.com
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 后续，左右中

        if not root:
            return 0

        leftH = self.minDepth(root.left)
        rightH = self.minDepth(root.right)

        if root.left is None and root.right:
            return rightH + 1

        if root.left and root.right is None:
            return leftH + 1

        return min(leftH, rightH) + 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 迭代法
        # 相当于找到第一个叶子结点
        if not root:
            return 0

        que = collections.deque()
        que.append(root)
        res = 1

        while que:
            for _ in range(len(que)):
                node = que.popleft()

                if not node.left and not node.right:
                    # 当节点的左右孩子都为空时，才算是最小深度
                    return res

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)
            # 遍历完一层，深度+1
            res += 1

        return res
