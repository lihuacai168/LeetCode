# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional

# @Author: 花菜
# @File: 145二叉树的后序遍历.py
# @Time : 2022/11/2 18:09
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 后序遍历，左右中
        def dfs(root, ans):
            if not root:
                return

            dfs(root.left, ans)
            dfs(root.right, ans)
            ans.append(root.val)

        ans = []
        dfs(root, ans)
        return ans
