# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional


# @Author: 花菜
# @File: 94二叉树的中序遍历.py
# @Time : 2022/11/2 18:08
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     def dfs(root, ans):
    #         if not root:
    #             return

    #         dfs(root.left, ans)
    #         ans.append(root.val)
    #         dfs(root.right, ans)
    #     ans = []
    #     dfs(root, ans)
    #     return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        cur = root
        # 中序，左中右
        while cur or stack:

            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right

        return ans
