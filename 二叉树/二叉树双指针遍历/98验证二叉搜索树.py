# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional


# @Author: 花菜
# @File: 98验证二叉搜索树.py
# @Time : 2022/11/2 17:08
# @Email: lihuacai168@gmail.com
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 中序，左中右，遍历结果递增
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = None

        def dfs(root):
            nonlocal pre
            if not root:
                return True

            left_result = dfs(root.left)

            if pre and root.val <= pre.val:
                return False
            pre = root
            right_result = dfs(root.right)
            return left_result and right_result

        return dfs(root)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = []
        stack.append(root)
        nums = []
        while stack:
            node = stack.pop()
            # 前序
            if node:
                nums.append(node.val)
            else:
                continue
            # 前序，左中右
            # 入栈左右需要反过来
            stack.append(node.right)
            stack.append(node.left)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = []
        cur = root
        # 中序， 左中右,123
        pre = None
        while cur or stack:
            if cur:
                stack.append(cur)
                # 左
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and pre.val >= cur.val:
                    return False
                pre = cur
                cur = cur.right
        return True
