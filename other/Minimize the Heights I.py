import heapq


def minimizeHeight(arr, k):
    arr.sort()
    minHeight = arr[0]
    maxHeight = arr[-1]
    print(arr, maxHeight, minHeight)

    if (maxHeight - minHeight) < k or (maxHeight - k) < (minHeight + k):
        heightDif = maxHeight - minHeight

    else:
        heightDif = (maxHeight - k) - (minHeight + k)

    return heightDif





arr = [2, 4, 3, 9, 9, 10, 9, 7, 1, 2]
k = 4

print(minimizeHeight(arr, k))