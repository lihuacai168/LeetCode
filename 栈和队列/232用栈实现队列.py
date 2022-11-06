# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 232用栈实现队列.py
# @Time : 2022/11/6 16:57
# @Email: lihuacai168@gmail.com


# 两个栈模拟队列


class MyQueue:
    def __init__(self):
        self._in = []
        self._out = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        # 优先弹出待出栈的元素
        if self._out:
            return self._out.pop()
        else:
            # 当待出栈的元素列表为空时，需要先处理已经入栈的元素
            # 队列是先进先出，栈是先进后出，所以需要把已经入栈的元素反过来
            while self._in:
                self._out.append(self._in.pop())
            return self._out.pop()

    def peek(self) -> int:
        val = self.pop()
        self._out.append(val)
        return val

    def empty(self) -> bool:
        return not (self._in or self._out)
