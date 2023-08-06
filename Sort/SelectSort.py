# 选择排序

"""
选择排序（Selection Sort）是一种简单直观的排序算法，其基本思想是在未排序的序列中，找到最小
（或最大）的元素，放到序列的起始位置，然后在剩余的未排序的序列中继续寻找最小（或最大）的元素，放到已排序序列的末尾，直到所有元素均排序完毕。它的具体实现方式是：

在未排序的序列中找到最小（或最大）的元素，并记录其位置；
将最小（或最大）的元素与序列的起始位置进行交换；
在剩余的未排序的序列中重复上述操作，不断扩大已排序序列的范围，直到所有元素均排序完毕。
"""
# 耗内存，会新建一个列表

def SelectSort(arr):
    new_list = []
    for time in range(len(arr)):
        # 获取最小值
        min_value = np.min(arr)
        # 添加新列表
        new_list.append(new_list)
        # 删除这个值
        np.delete(arr,np.where(arr==min_value))
    return new_list
