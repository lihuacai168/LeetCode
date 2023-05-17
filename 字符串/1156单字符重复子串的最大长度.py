# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 1156单字符重复子串的最大长度.py
# @Time : 2023/5/17 19:21
# @Email: lihuacai168@gmail.com


# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
#
# 给你一个字符串
# text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
#
#
#
# 示例
# 1：
#
# 输入：text = "ababa"
# 输出：3
# 示例
# 2：
#
# 输入：text = "aaabaaa"
# 输出：6
# 示例
# 3：
#
# 输入：text = "aaabbaaa"
# 输出：4
# 示例
# 4：
#
# 输入：text = "aaaaa"
# 输出：5
# 示例
# 5：
#
# 输入：text = "abcdef"
# 输出：1
#
# 提示：
#
# 1 <= text.length <= 20000
# text
# 仅由小写英文字母组成。


from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # 滑动窗口 + 哈希表
        # 判断当前的字符是否等于前一个字符
        # 如果是，直接更新当前字符数量；如果不是，从下一位开始往后搜索，搜索条件是索引小于text长度，并且下一个字符和当前字符相等；
        # 然后判断当前字符数量是否已经是最大值，如果不是，就+1
        # 然后更新最长相同字符串
        # 重置当前字符，和当前字符数量

        if len(text) == 1:
            return 1

        count = Counter(text)

        pre_char = text[0]
        pre_char_count = 1
        max_len = 0

        for i in range(1, len(text)):
            cur_char = text[i]
            if pre_char == cur_char:
                pre_char_count += 1
            else:

                search_index = i + 1
                while search_index < len(text) and text[search_index] == pre_char:
                    pre_char_count += 1
                    search_index += 1

                if pre_char_count < count[pre_char]:
                    pre_char_count += 1

                max_len = max(max_len, pre_char_count)

                # 重置当前字符
                pre_char = cur_char
                pre_char_count = 1

        if pre_char_count < count[pre_char]:
            pre_char_count += 1

        max_len = max(max_len, pre_char_count)

        return max_len


s = Solution()
s.maxRepOpt1("aabbaa")
