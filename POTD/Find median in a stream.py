# def getMedian(arr):
#     n = len(arr)
#     list = [arr[0]]
#
#     medianList = [0.0 for _ in range(n)]
#
#     medianList[0] = float(list[0])
#
#     for i in range(1, n):
#         list.append(arr[i])
#         if i == 1:
#             medianList[1] = float((list[0] + list[1]) / 2)
#         else:
#             list.sort()
#             index = (i // 2)
#             if i % 2 == 1:
#                 medianList[i] = float((list[index] + list[index + 1]) / 2)
#             else:
#                 medianList[i] = float(list[index])
#
#     return medianList


# Python program to find Median from Running Data Stream
# Using Heaps

import heapq


def getMedian(arr):
    leftMaxHeap = []

    rightMinHeap = []

    res = []

    for num in arr:
        heapq.heappush(leftMaxHeap, -num)
        print(leftMaxHeap)

        temp = -heapq.heappop(leftMaxHeap)

        heapq.heappush(rightMinHeap, temp)

        if len(rightMinHeap) > len(leftMaxHeap):
            temp = heapq.heappop(rightMinHeap)
            heapq.heappush(leftMaxHeap, -temp)

        if len(leftMaxHeap) != len(rightMinHeap):
            median = -leftMaxHeap[0]
        else:
            median = (-leftMaxHeap[0] + rightMinHeap[0]) / 2.0

        res.append(median)

    return res


if __name__ == "__main__":
    arr = [5, 15, 1, 3, 2, 8]
    res = getMedian(arr)

    print(" ".join(f"{median:.2f}" for median in res))

arr = [4, 3, 1, 29, 24, 22, 22, 6, 15, 2, 1]
print(getMedian(arr))

# 4.0 3.5 3.0 3.5 4.0 13.0 22.0 14.0 15.0 10.5 6.0