# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 二叉树.py
# @Time : 2021/8/23 23:13
# @Email: lihuacai168@gmail.com
import collections

from loguru import logger


def dfs(root):
    """深度优先遍历"""
    if not root:
        return
    logger.debug(f"{root.val}")
    dfs(root.left)
    dfs(root.right)


def bfs(root):
    """广度优先遍历"""
    q = collections.deque([root])
    while q:
        size = len(root)
        for _ in range(size):
            node = q.popleft()
            logger.debug(f"{node.val}")
            left, right = node.left, node.right
            if left:
                q.push(left)
            if right:
                q.push(right)
            logger.debug("当前层遍历完成")
