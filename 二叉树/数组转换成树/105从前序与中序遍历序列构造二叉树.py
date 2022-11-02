# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List, Optional

# @Author: 花菜
# @File: 105从前序与中序遍历序列构造二叉树.py
# @Time : 2022/11/2 15:46
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preoder 中左右
        # inorder 左中右

        if not preorder:
            return

        # 根据前序确定node节点的值 root_val = preorder[0]
        # 根据前序 root_val切割 inorder，分成左中序，后右中序

        # 根据左中序切割preorder，分成左前序，右前序

        root_val = preorder[0]
        root = TreeNode(root_val)
        if len(preorder) == 1:
            return root

        spe_idx = inorder.index(root_val)

        # 左闭右开
        left_inorder = inorder[:spe_idx]
        right_inorder = inorder[spe_idx + 1 :]

        # 前序数组长度需要和中序数组长度一样
        # 前序需要排除第一个排除头节点，index从1开始，截取len(left_inorder)个元素
        left_preorder = preorder[1 : len(left_inorder) + 1]
        right_preoder = preorder[1 + len(left_inorder) :]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preoder, right_inorder)
        return root
