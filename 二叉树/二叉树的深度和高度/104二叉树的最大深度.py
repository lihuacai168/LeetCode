# !/usr/bin/python3
# -*- coding: utf-8 -*-
import collections
from typing import Optional

# @Author: 花菜
# @File: 104二叉树的最大深度.py
# @Time : 2022/11/2 17:42
# @Email: lihuacai168@gmail.com


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        height = max(leftHeight, rightHeight) + 1

        return height

    def maxDepth(self, root) -> int:
        if not root:
            return 0

        que = collections.deque()
        que.append(root)
        res = 0

        while que:
            for i in range(len(que)):
                node = que.popleft()

                if i == 0:
                    # 每遍历一层就+1
                    res += 1

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

        return res
