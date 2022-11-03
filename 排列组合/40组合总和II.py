# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import List


# @Author: 花菜
# @File: 40组合总和II.py
# @Time : 2022/11/2 23:05
# @Email: lihuacai168@gmail.com


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 去重的前提是数组有序
        candidates.sort()
        path = []

        def backtracking(candidates, path_sum, paths, start_index, target):
            if path_sum > target:
                # 剪枝
                return

            if path_sum == target:
                # 收获结果集
                paths.append(path[:])

            for i in range(start_index, len(candidates)):
                if candidates[i] > target:
                    # 剪枝
                    break

                if i > start_index and candidates[i] == candidates[i - 1]:
                    # 注意i需要大于歧视位置,因为有i-1的取值
                    # 树枝和树层都去重
                    continue

                path.append(candidates[i])
                path_sum += candidates[i]

                backtracking(candidates, path_sum, paths, i + 1, target)
                # 回溯
                path.pop()
                path_sum -= candidates[i]

        paths = []
        backtracking(candidates, 0, paths, 0, target)

        return paths
