# def stockSpan(arr):
#     n = len(arr)
#     res = [1]*n
#
#     for i in range(n - 1, 0, -1):
#         for j in range(i - 1, -1, -1):
#             if arr[j] <= arr[i]:
#                 res[i] += 1
#             else:
#                 break
#     return res

# ------------------------------------------------
# def stockSpan(arr):
#     n = len(arr)
#     res = [1]*n
#
#     for i in range(n - 1, 0, -1):
#         smaller = 1
#         for j in range(i):
#             if arr[j] > arr[i]:
#                 smaller = 1
#             else:
#                 smaller += 1
#         res[i] = smaller
#     return res

# --------------------------------------------------
def stockSpan(arr):
    n = len(arr)
    res = [0] * n
    stk = []

    for i in range(n):
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        if not stk:
            res[i] = i + 1
        else:
            res[i] = i - stk[-1]

        stk.append(i)

    return res


arr = [10, 4, 5, 90, 120, 80, 90, 100]
print(stockSpan(arr))
#  [1, 1, 2, 4, 5, 1]