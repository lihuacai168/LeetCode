# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 19:31
# @Author  : lihuacai
# @Email   : lihuacai168@gmail.com
# @File    : 快速排序1.py
# @Software: PyCharm
import time


def partition(arr, low, high):
    pivot_index = low
    pivot = arr[pivot_index]
    left = pivot_index + 1
    right = high - 1
    while True:

        # 从arr的第2个元素遍历,left索引小于等于right,并且left元素小于pivot时,left+1继续循环,直到条件不满足
        # 退出循环时,证明left>right 或者 arr[left] >pivot
        while left <= right and arr[left] < pivot:
            left += 1
        while right >= left and arr[right] >= pivot:
            right -= 1

        # 循环出口
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 上面循环结束时,right就是arr分界线的索引
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    return right

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot)
        quick_sort(arr, pivot + 1, high)

import random
if __name__ == '__main__':
    arr = list(range(997))
    # random.shuffle(arr)
    # print(arr)

    arr = arr[::-1]
    print("*" * 100)
    start = time.time()
    quick_sort(arr, 0, len(arr))
    print(time.time() - start)
    # arr.sort()
    print(arr)