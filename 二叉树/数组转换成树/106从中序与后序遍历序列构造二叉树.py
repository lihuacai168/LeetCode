# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional


# @Author: 花菜
# @File: 106从中序与后序遍历序列构造二叉树.py
# @Time : 2022/11/2 15:47
# @Email: lihuacai168@gmail.com
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 确定中序的切割点, 也是root节点，postorder[-1]
        # 构建root节点
        # 切割得到中序的左子树，和右子树

        # 根据中序左子树切割后续的左子树和右子树
        if not inorder:
            return

        sep_idx = inorder.index(postorder[-1])
        root = TreeNode(postorder[-1])

        # 左闭右开
        leftInorder = inorder[:sep_idx]
        rightInorder = inorder[sep_idx + 1 :]

        leftPostorder = postorder[: len(leftInorder)]
        rightPostorder = postorder[len(leftInorder) : -1]

        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)

        return root
