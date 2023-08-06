# 插入排序
def InsertSort(arr):
    """
    打扑克，插牌
    """
    for i in range(1,len(arr)):
        tmp = arr[i]  # 每次抓的牌
        j = i -1 #手里最后一张牌的下标
        while j >= 0  and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
        return arr
