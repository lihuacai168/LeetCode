# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 501二叉搜索树中的众数.py
# @Time : 2022/11/2 17:04
# @Email: lihuacai168@gmail.com
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count, maxCount = 0, 0
        pre = None
        ans = []

        def dfs(node):
            if not node:
                return

            nonlocal count, maxCount, pre, ans
            dfs(node.left)

            if not pre:
                # 第一个节点的时候
                count = 1
            elif pre.val == node.val:
                # 前后节点相同
                count += 1
            else:
                # 前后节点不相同，主要重置count，不能用count -= 1
                count = 1

            pre = node
            if count == maxCount:
                # 多个众数的情况
                ans.append(node.val)

            if count > maxCount:
                # 清空之前的众数，并且更新最大众数数值
                maxCount = count
                ans.clear()
                ans.append(node.val)

            dfs(node.right)

        dfs(root)
        return ans
