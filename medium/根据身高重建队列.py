# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 根据身高重建队列.py
# @Time : 2020/11/17 01:20
# @Email: lihuacai168@gmail.com
from typing import List

"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对 (h, k) 表示，其中 h 是这个人的身高，k 是应该排在这个人前面且身高大于或等于 h 的人数。 例如：[5,2] 表示前面应该有 2 个身高大于等于 5 的人，而 [5,0] 表示前面不应该存在身高大于等于 5 的人。

编写一个算法，根据每个人的身高 h 重建这个队列，使之满足每个整数对 (h, k) 中对人数 k 的要求。

示例：

输入：[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
输出：[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
 

提示：

总人数少于 1100 人。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    """
    >>> s = Solution()
    >>> res = s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    >>> res == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    True
    """
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        n = len(people)
        ans = list()
        for person in people:
            t = person[1]
            ans[person[1]:person[1]] = [person]
        return ans


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照身高降序排序，按照人数降序排序
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for person in people:
            # 已经按照身高降序排好顺序后
            # 身高相同时，人数越多的排在后面，person[1]的值正好就是person所在的位置
            # list指定插入
            # a = [1,2,3]
            # a[1:1] = [[4,5]]
            # a会变成[1,[4,5],2,3]
            ans[person[1]:person[1]] = [person]
        return ans

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
