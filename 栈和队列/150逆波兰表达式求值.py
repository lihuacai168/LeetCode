# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 150逆波兰表达式求值.py
# @Time : 2022/11/6 18:03
# @Email: lihuacai168@gmail.com


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                # 除法和减法时，需要需要num1和num2的前后顺序
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num2 - num1
                elif token == "*":
                    res = num2 * num1
                elif token == "/":
                    res = num2 / num1
                stack.append(int(res))
        return int(stack.pop())
