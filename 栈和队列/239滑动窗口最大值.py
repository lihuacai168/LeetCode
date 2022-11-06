# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 239滑动窗口最大值.py
# @Time : 2022/11/6 18:05
# @Email: lihuacai168@gmail.com

from collections import deque
from typing import List


class MyQueue:
    # 单调队列，第一个元素最大，后面的元素单调递减
    # push的时候，需要判断当前要push的元素是不是比q里面的要大，
    # 如果是，需要把q里面那些小的元素全部弹出来；否则直接push就行

    # pop的时候，只需要判断滑动窗口左侧的值是否和q的第一个元素相等
    # 如果是，那就pop，否则不需操作
    def __init__(self):
        self.que = deque()

    def pop(self, val):
        if self.que and val == self.que[0]:
            self.que.popleft()

    def push(self, val):
        while self.que and val > self.que[-1]:
            self.que.pop()
        self.que.append(val)

    def get_max(self):
        return self.que[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = MyQueue()
        for i in range(k):
            q.push(nums[i])
        ans.append(q.get_max())

        for j in range(k, len(nums)):
            # 向右移动窗口
            q.push(nums[j])  # 窗口右侧
            q.pop(nums[j - k])  # 窗口左侧
            ans.append(q.get_max())  # 当前窗口最大值
        return ans
