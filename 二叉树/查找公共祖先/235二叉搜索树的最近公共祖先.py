# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 235二叉搜索树的最近公共祖先.py
# @Time : 2022/11/2 16:47
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # 利用二叉搜索树的特性，左 < 中 < 右
        # 递归或者迭代都能实现

        ans = root
        while 1:
            if p.val < ans.val and q.val < ans.val:
                ans = ans.left

            elif p.val > ans.val and q.val > ans.val:
                ans = ans.right
            else:
                return ans

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        if not root:
            return

        if p.val < root.val and q.val < root.val:
            node = self.lowestCommonAncestor(root.left, p, q)
            if node:
                return node

        elif p.val > root.val and q.val > root.val:
            node = self.lowestCommonAncestor(root.right, q, p)
            if node:
                return node

        else:
            return root
