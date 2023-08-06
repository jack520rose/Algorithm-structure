# 堆排序

# 向下函数
def shift(arr:list,low,high):
    """
    大顶堆
    arr : 数组
    low : 堆的根节点
    high: 堆的最后一个元素，作用是判断是否越界
    """
    i = low  # i最开始指向根节点
    j = 2*i +1  # j开始左孩子
    tmp = arr[low] # 把堆顶存起来
    while j <= high : # 需要存在左孩子
        if j+1 <= high and arr[j+1] > arr[j]: # 存在右孩子且右孩子大于左孩子
            j += 1
        if arr[j] > tmp: # 当根节点的数据小于下一节点的孩子的情况
            arr[i] = arr[j] # 把孩子放上来，孩子位置空着
            i = j  # low转为孩子下标
            j = 2*i + 1 # 继续查找下一个孩子节点
        else:
            break  # 当他不存在比他大的孩子节点则退出
    arr[i] = tmp  # 把孩子节点的空位补充进去


def HeapSort(arr):
    length = len(arr) # 数组长度
    # 建立堆
    for i in range((length-2)//2,-1,-1): # 从最后一个子根节点开始
        # i 表示调整根的下标
        shift(arr,i,length-1) # 这边high为了方便使用，就使用最后一个节点
        # print(arr)
    # 建堆完成
    # 进行挨个出数
    for i in range(length-1,-1,-1): # 从最后一个节点开始，所以是length-1
        arr[0],arr[i] = arr[i],arr[0] # 最后一个节点与根节点进行互换
        shift(arr,0,i-1) # 因为孩子节点上去了所以需要进行向下进行处理，但需要排除换位的最后一个节点，i-1
