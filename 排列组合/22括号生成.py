# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 22括号生成.py
# @Time : 2022/11/7 15:26
# @Email: lihuacai168@gmail.com

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 8
#
#
#  Related Topics 字符串 动态规划 回溯 👍 2941 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(path: list, left: int, right: int):
            if len(path) == 2 * n:
                ans.append(''.join(path))
                return

            if left < n:
                path.append("(")
                backtracking(path, left + 1, right)
                path.pop()

            if right < left:
                path.append(")")
                backtracking(path, left, right + 1)
                path.pop()

        backtracking([], 0, 0)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
