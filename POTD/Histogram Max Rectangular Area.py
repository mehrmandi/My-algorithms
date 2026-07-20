
# def maxRectangular(arr):
#     n = len(arr)
#     res = [0] * n
#
#     for i in range(n):
#         height = arr[i]
#         width = 0
#         for j in range(i, n):
#             if arr[i] == 0:
#                 break
#             if arr[j] < height:
#                 height = arr[j]
#             width += 1
#             res[j] = max(height * width, res[j])
#
#     return max(res)
#

# Python program to find the largest rectangular area possible
# in a given histogram

# Function to calculate the maximum rectangular area
def getMaxArea(arr):
    n = len(arr)
    s = []
    res = 0


    for i in range(n):
        while s and arr[s[-1]] >= arr[i]:
            tp = s.pop()
            width = i if not s else i - s[-1] - 1

            res = max(res, arr[tp] * width)

        s.append(i)

    while s:
        tp = s.pop()
        width = n if not s else n - s[-1] - 1
        res = max(res, arr[tp] * width)

    return res


arr = [60, 20, 50, 40, 10, 50, 60]

# [347, 411, 476, 253, 314, 495, 959, 158, 541]

print(getMaxArea(arr))



