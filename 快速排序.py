def partition(L, low, high):  # 进行一趟排序
    key = L[low]  # 存储key值
    while low < high:
        while low < high and L[high] > key:  # 从右往左找小
            high -= 1
        L[low] = L[high]
        while low < high and L[low] < key:  # 从左往右找大
            low += 1
        L[high] = L[low]

    L[low] = key
    print(L, low)  ##打印每一趟排序结果和Key的位置
    return low  # 返回这趟排序结束后的key的位置


def sort(L, low, high):
    if low < high:
        index = partition(L, low, high)
        sort(L, low, index)
        sort(L, index + 1, high)


L = [49, 38, 65, 97, 76, 13, 27]
sort(L, 0, len(L) - 1)
print(L)
