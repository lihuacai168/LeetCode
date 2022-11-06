# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 242有效的字母异位词.py
# @Time : 2022/11/5 18:14
# @Email: lihuacai168@gmail.com


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 使用字典作为哈希表，统计每个元素出现的个数
        # 最后比较所有元素的个数
        m1 = {}
        m2 = {}
        for k in s:
            m1[k] = m1.get(k, 0) + 1

        for k in t:
            m2[k] = m2.get(k, 0) + 1

        return m1 == m2

    def isAnagram(self, s: str, t: str) -> bool:
        # 使用列表作为哈希表
        # 字符串只有小写字母，可以直接枚举所有字母
        # 小写字母作为列表的index，次数就是index对应的值
        hash_arr = [0] * 26
        for ch in s:
            hash_arr[ord(ch) - ord("a")] += 1

        for ch in t:
            hash_arr[ord(ch) - ord("a")] -= 1

        for ch_count in hash_arr:
            if ch_count != 0:
                return False
        return True
