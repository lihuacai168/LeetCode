# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 有效的字母异位词.py
# @Time : 2020/11/22 13:00
# @Email: lihuacai168@gmail.com

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        return Counter(s) == Counter(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = [i for i in s]
        s.sort()
        t = [i for i in t]
        t.sort()
        return s == t