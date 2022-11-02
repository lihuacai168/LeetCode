# !/usr/bin/python3
# -*- coding: utf-8 -*-
import collections
from typing import List, Optional


# @Author: 花菜
# @File: 102二叉树的层序遍历.py
# @Time : 2022/11/2 18:06
# @Email: lihuacai168@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        que = collections.deque()
        # 初始化队列
        que.append(root)

        # 当队列里面有值，都继续遍历
        while que:
            # 创建一个列表记录当前层的数据
            cur_level = []
            # 当前层元素的个数
            size = len(que)

            # 遍历当前层的元素
            for _ in range(size):
                node = que.popleft()
                # 把当前层的元素记下来
                cur_level.append(node.val)

                # 把当前层节点的左右孩子加入到队列，下一次循环中会处理
                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

            # 把当前层的所有元素加入到结果中
            result.append(cur_level)
        return result
