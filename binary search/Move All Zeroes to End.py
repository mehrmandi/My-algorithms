# def move_zero_right(arr):
#     n = len(arr)
#     i = 0
#     j = 0
#
#     while i < n and j <= n:
#         if arr[i] == 0:
#             arr.pop(i)
#             arr.append(0)
#             j += 1
#         else:
#             i += 1
#             j += 1
#
#     return arr
#
#
#

def move_zero_right(arr):
    i = 0
    n = len(arr)

    while i < len(arr):
        if arr[i] == 0:
            arr.pop(i)
        else:
            i += 1

    print(arr)

    for i in range(n - len(arr)):
        arr.append(0)

    return arr


arr = [3, 5, 0, 0, 4]

print(move_zero_right(arr))