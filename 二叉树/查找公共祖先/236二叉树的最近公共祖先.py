# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 236二叉树的最近公共祖先.py
# @Time : 2022/11/2 16:46
# @Email: lihuacai168@gmail.com


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # 后序，左右中
        # 遇到p或者q时，向上返回节点，需要接收这个值
        # 对左右子树搜索返回值判断
        # 例子2中，不需要特殊考虑，因为先找到5,不再向下遍历，直接返回5, 相当于3的左子树

        if not root:
            return
        if root.val in (p.val, q.val):
            return root
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        # print(root.val)
        if left_res and right_res:
            # print(root.val)
            return root

        if left_res and not right_res:
            # print(root.val)
            return left_res
        elif right_res and not left_res:
            return right_res
        else:
            return None
