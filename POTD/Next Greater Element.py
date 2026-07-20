# def nextGreaterElement(arr):
#     n = len(arr)
#     res = [-1] * n
#
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[j] > arr[i]:
#                 print(i, j)
#                 res[i] = arr[j]
#                 break
#
#     return res
# User function Template for python3



def nextLargerElement(arr):
    # code here
    n = len(arr)
    res = [-1] * n
    stk = []

    for i in range(n - 1, -1, -1):

        while stk and arr[stk[-1]] >= arr[i]:
            stk.pop()

        if stk:
            print(i, stk[-1])
            res[i] = stk[-1]
            print(res)

        stk.append(i)

    return res




# arr = [6, 8, 0, 1, 3]
# arr = [57, 78, 5, 21, 90, 50, 0, 46, 18, 42, 57, 78, 5, 21, 90, 50, 0, 46, 18, 42]
# [78, 90, 21, 90, -1, 57, 46, 57, 42, 57, 78, 90, 21, 90, -1, -1, 46, -1, 42, -1]
# [78, 90, 21, 90, -1, 57, 46, 57, 42, 57, 78, 90, 21, 90, -1, -1, 46, -1, 42, -1]
arr = [4, 5, 1, 6, 7, 9, 1, 6, 4]
print(nextLargerElement(arr))
