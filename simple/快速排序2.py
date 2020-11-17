# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 19:37
# @Author  : lihuacai
# @Email   : lihuacai168@gmail.com
# @File    : 快速排序2.py
# @Software: PyCharm
import time


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
if __name__ == '__main__':


    arr = list(range(997))
    arr = arr[::-1]
    n = len(arr)
    start = time.time()
    quickSort(arr, 0, n - 1)
    print(time.time() - start)
    print("Sorted array is:")
    print(arr)