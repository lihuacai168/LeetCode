# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 三角形的最大周长.py
# @Time : 2020/11/29 20:28
# @Email: lihuacai168@gmail.com
"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。

 

示例 1：

输入：[2,1,2]
输出：5
示例 2：

输入：[1,2,1]
输出：0
示例 3：

输入：[3,2,3,4]
输出：10
示例 4：

输入：[3,6,2,3]
输出：8
 

提示：

3 <= A.length <= 10000
1 <= A[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-perimeter-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    """
    >>> s = Solution()
    >>> s.largestPerimeter([2,1,2]) == 5
    True

    """
    # 倒叙遍历
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        ans = 0
        A.sort()
        j = n - 3
        while j >= 0:
            l = A[j:j + 3]
            if len(l) < 3:
                break
            if self.is_angle(l):
                ans = sum(l)
                break
            j -= 1
        return ans

    # 顺序遍历
    def largestPerimeter(self, A):

        n = len(A)
        if n < 3:
            return 0
        ans = 0
        A.sort(reverse=True)
        i = 0
        while i <= n - 3:
            l = A[i:i+3]
            if len(l) < 3:
                break
            if self.is_angle(l):
                ans = sum(l)
                break
            i += 1
        return ans

    def is_angle(self, l):
        if l[0] + l[1] > l[2] and l[1] + l[2] > l[0] and l[2] + l[0] > l[1]:
            return True
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
