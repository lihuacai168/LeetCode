# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 二分查找.py
# @Time : 2020/12/11 21:15
# @Email: lihuacai168@gmail.com

# 递归实现
def binarySearch(arr: list, l: int, r: int, target: int) -> int:
    """
    >>> binarySearch([0, 1, 2, 3, 4, 5], 0, 5, 7)
    -1

    >>> binarySearch([0, 1, 2, 3, 4, 5], 0, 5, 3)
    3

    >>> binarySearch([0, 1, 2, 3, 4, 5], 0, 5, 1)
    1

    >>> binarySearch([0, 1, 2, 3, 4, 5], 0, 5, 4)
    4

    >>> binarySearch([0, 1, 2, 3, 4, 5], 0, 5, 0)
    0

    >>> binarySearch([0, 1, 2, 3, 4, 5], 0, 5, 5)
    5

    >>> binarySearch([0, 1, 2, 3, 4, 5, 10], 0, 6, 10)
    6
    """
    if len(arr) == 0 or l > r:
        return -1

    mid = int((l + r)/2)

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        l = mid + 1
        return binarySearch(arr, l, r, target)
    else:
        r = mid - 1
        return binarySearch(arr, l, r, target)


def bin_search(arr: list, find_val: int):
    """
    时间复杂度O(log2(n))
    空间复杂度O(1)
    >>> bin_search([0, 1, 2, 3, 4, 5],7)
    -1

    >>> bin_search([0, 1, 2, 3, 4, 5],3)
    3

    >>> bin_search([0, 1, 2, 3, 4, 5],1)
    1

    >>> bin_search([0, 1, 2, 3, 4, 5],4)
    4

    >>> bin_search([0, 1, 2, 3, 4, 5],0)
    0                                                           

    >>> bin_search([0, 1, 2, 3, 4, 5],5)
    5

    >>> bin_search([0, 1, 2, 3, 4, 5, 10],10)
    6
    """
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = (high + low) // 2
        if arr[mid] == find_val:
            return mid
        else:
            if arr[mid] < find_val:
                low = mid + 1
            else:
                high = mid - 1
    return -1

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
