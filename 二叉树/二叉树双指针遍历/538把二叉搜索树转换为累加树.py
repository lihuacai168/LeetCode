# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Optional


# @Author: 花菜
# @File: 538把二叉搜索树转换为累加树.py
# @Time : 2022/11/2 15:29
# @Email: lihuacai168@gmail.com

# https://leetcode.cn/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 后续遍历，右 中 左

        # 双指针法
        # 通过后续遍历的方式，把前一个节点的值加到当前节点
        # 然后更新双指针的位置

        # 初始化后一个指针为空，因为0加上当前节点的值，也等于当前节点
        pre = 0

        def dfs(root):
            if not root:
                return
            dfs(root.right)  # 右
            nonlocal pre
            root.val += pre  # 中 更新当前节点的值
            pre = root.val  # 更新后一个指针
            dfs(root.left)  # 左

        dfs(root)
        return root
