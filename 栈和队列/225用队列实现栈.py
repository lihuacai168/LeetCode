# !/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import deque

# @Author: 花菜
# @File: 225用队列实现栈.py
# @Time : 2022/11/6 17:36
# @Email: lihuacai168@gmail.com


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        # 弹出前n-1个元素，最后一个就是出栈的元素
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        return self.q.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.q[-1]

    def empty(self) -> bool:
        if not self.q:
            return True
        return False
