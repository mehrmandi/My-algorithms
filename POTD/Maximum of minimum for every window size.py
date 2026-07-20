# def maxMinArray(arr, index, n):
#     minArray = []
#     for i in range(n - index + 1):
#         item = float('inf')
#         for j in range(i, i + index):
#             if arr[j] < item:
#                 item = arr[j]
#         minArray.append(item)
#     return max(minArray)
#
#
# def maxOfMins(arr):
#     n = len(arr)
#     res = [0]*n
#
#     for i in range(n):
#         res[i] = maxMinArray(arr, i + 1, n)
#
#     return res


def maxOfMins(arr):
    n = len(arr)
    res = [0] * n
    s = []

    lenArr = [0] * n

    for i in range(n):

        while s and arr[s[-1]] >= arr[i]:
            print("aval", s, i)
            top = s.pop()
            windowSize = i if not s else i - s[-1] - 1
            print("aval size", windowSize)
            lenArr[top] = windowSize
            print("aval len", lenArr)
        print("append", i)
        s.append(i)

    while s:
        print("sec", s)
        top = s.pop()
        windowSize = n if not s else n - s[-1] - 1
        print("sec size", windowSize)
        lenArr[top] = windowSize
        print("sec len", lenArr)

    for i in range(n):
        windowSize = lenArr[i] - 1
        print("third size", windowSize, res)
        res[windowSize] = max(res[windowSize], arr[i])

    for i in range(n - 2, -1, -1):
        print("akhar", i, res)
        res[i] = max(res[i], res[i + 1])

    return res



arr = [10, 20, 30, 50, 10, 70, 30]
print(maxOfMins(arr))







