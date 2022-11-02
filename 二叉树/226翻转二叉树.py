# !/usr/bin/python3
# -*- coding: utf-8 -*-
import collections
from typing import List, Optional

# @Author: 花菜
# @File: 226翻转二叉树.py
# @Time : 2022/11/2 17:54
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root: return

    #     # 深度优先，中序递归
    #     root.left, root.right = root.right, root.left
    #     self.invertTree(root.left)
    #     self.invertTree(root.right)
    #     return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 广度优先，层序遍历

        if not root:
            return root
        que = collections.deque()
        que.append(root)

        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                node.left, node.right = node.right, node.left

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)
        return root
