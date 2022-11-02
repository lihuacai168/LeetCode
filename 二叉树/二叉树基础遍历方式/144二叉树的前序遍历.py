# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional

# @Author: 花菜
# @File: 144二叉树的前序遍历.py
# @Time : 2022/11/2 18:10
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 前序遍历，中左右
        def dfs(root, ans):
            if not root:
                return

            ans.append(root.val)
            dfs(root.left, ans)
            dfs(root.right, ans)

        ans = []
        dfs(root, ans)
        return ans
