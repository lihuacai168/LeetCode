# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional

# @Author: 花菜
# @File: 513找树左下角的值.py
# @Time : 2022/11/2 16:54
# @Email: lihuacai168@gmail.com


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

    #     if not root: return 0

    #     que = collections.deque()
    #     que.append(root)

    #     while que:
    #         size = len(que)
    #         for i in range(size):
    #             # 层序遍历，获取当前层的第一个元素
    #             if i == 0:
    #                 leftValue = que[0].val

    #             node = que.popleft()
    #             if node.left:
    #                 que.append(node.left)

    #             if node.right:
    #                 que.append(node.right)

    #     return leftValue

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxDepth = -1
        val = 0
        # 计算二叉树的最大深度，并且记录最大深度对应的元素值

        def dfs(node, depth):
            nonlocal maxDepth, val
            if not node.left and not node.right:
                if depth > maxDepth:
                    maxDepth = depth
                    val = node.val

            if node.left:
                depth += 1
                dfs(node.left, depth)
                # 计算子树深度时，需要回溯，否则depth会无限增大
                depth -= 1

            if node.right:
                depth += 1
                dfs(node.right, depth)
                depth -= 1

        dfs(root, 1)
        return val
