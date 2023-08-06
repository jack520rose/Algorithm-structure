# 冒泡排序

"""
冒泡排序（Bubble Sort）是一种简单直观的排序算法，其基本思想是通过交换相邻的元素，
将较大的元素逐渐“冒泡”到数组的末尾，实现对数组的排序。它的具体实现方式是：
从数组的第一个元素开始，比较相邻的两个元素，如果第一个元素比第二个元素大，则交换它们的位置；
继续比较相邻的两个元素，直到将最大的元素“冒泡”到数组的末尾；
重复上述过程，每一轮比较都将数组中最大的元素“冒泡”到末尾；
最终得到一个有序的数组。
"""
def BubbleSort(arr):
    #
    for traverse_time in range(len(arr)):
        #
        for j in range(len(arr)-traverse_time-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr
