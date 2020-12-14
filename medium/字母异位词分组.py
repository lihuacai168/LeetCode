# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 字母异位词分组.py
# @Time : 2020/12/14 00:40
# @Email: lihuacai168@gmail.com
from typing import List


class Solution:
    """
    >>> s = Solution()
    >>> s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["ate","eat","tea"],["nat","tan"],["bat"]]
    True
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        for word in strs:
            k = ''.join(sorted(word))
            if d.get(k, False):
                d[k].append(word)
            else:
                d[k] = [word]
        return list(d.values())


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
