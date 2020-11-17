# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author:梨花菜
# @File: LinkList.py
# @Time : 2020/9/3 22:10
# @Email: lihuacai168@gmail.com
# @Software: PyCharm
import time


def bubble(arr):
    """
    >>> arr = [3,1,2,4]
    >>> bubble(arr)
    >>> arr == [1, 2, 3, 4]
    True
    """
    if len(arr) <= 1:
        return arr
    length = len(arr)
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    min_part = []
    max_part = []
    flag = arr[0]
    for i in arr[1:]:
        if i < flag:
            min_part.append(i)
        else:
            max_part.append(i)
    return quick_sort(min_part) + [flag] + quick_sort(max_part)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
