# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional

# @Author: 花菜
# @File: 701二叉搜索树中的插入操作.py
# @Time : 2022/11/2 16:13
# @Email: lihuacai168@gmail.com


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 左中右，中序遍历

        def dfs(root, val):
            # 遍历到叶子节点时，返回节点
            if not root:
                return TreeNode(val)

            if root.val > val:
                # 二叉搜索树特性，当val比root值小，往左搜索
                root.left = dfs(root.left, val)
            else:
                root.right = dfs(root.right, val)

            return root

        return dfs(root, val)

        return dfs(root, val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 模拟递归
        if not root:
            return TreeNode(val)

        cur = root
        new_node = TreeNode(val)

        while cur:
            if val > cur.val:
                if not cur.right:
                    cur.right = new_node
                    break
                else:
                    cur = cur.right
            else:
                if not cur.left:
                    cur.left = new_node
                    break
                else:
                    cur = cur.left
        return root
