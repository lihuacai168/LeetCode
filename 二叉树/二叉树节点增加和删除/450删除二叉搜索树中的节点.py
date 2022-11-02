# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional


# @Author: 花菜
# @File: 450删除二叉搜索树中的节点.py
# @Time : 2022/11/2 16:06
# @Email: lihuacai168@gmail.com
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        # 找不到要删除的节点
        # 要删除的节点是左叶子节点，返回空
        # 要删除的节点不是叶子节点，节点的左子树为空，返回节点的右子树
        # 要删除的节点不是叶子节点，节点的右子树为空，返回节点的左子树
        # 要删除的节点不是叶子节点，节点的左右都不为空，保存当前节点右子树cur，遍历当前节点的右子树的左子树cur.left，直到退出
        # 把root.left当前节点的左子树赋值给,当前退出时的左子树cur.left
        # 最后一部，就相当于当前节点的左子树为空，右子树不为空，返回当前节点的右子树

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.left and not root.right:
                return None

            if not root.left and root.right:
                return root.right

            if not root.right and root.left:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            return root.right

        return root
