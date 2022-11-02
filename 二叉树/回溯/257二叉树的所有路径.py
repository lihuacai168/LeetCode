# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional


# @Author: 花菜
# @File: 257二叉树的所有路径.py
# @Time : 2022/11/2 17:30
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        def dfs(root, path, paths):
            # path.append(str(root.val))

            if not root.left and not root.right:
                paths.append("->".join(path))

            if root.left:
                path.append(str(root.left.val))
                dfs(root.left, path, paths)
                path.pop()

            if root.right:
                path.append(str(root.right.val))
                dfs(root.right, path, paths)
                path.pop()

        ans = []
        dfs(root, [str(root.val)], ans)
        return ans
