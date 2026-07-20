
# 11111111111111111111111

# def smallest_missing(arr):
#     set_arr = list(set(arr))
#     set_arr.sort()
#     num = 1
#     n = len(set_arr)
#     if set_arr[n - 1] <= 0:
#         return 1
#
#     for i in range(n):
#         if set_arr[i] > 0:
#             if set_arr[i] == num:
#                 num += 1
#
#             else:
#                 return num
#
#     return set_arr[n - 1] + 1
#
#
#
# arr = [-5]
#
# print(smallest_missing(arr))

# 222222222222222222222222222
# def missingNumber(arr):
#     n = len(arr)
#
#     # To mark the occurrence of elements
#     vis = [False] * n
#     for i in range(n):
#
#         # if element is in range from 1 to n
#         # then mark it as visited
#         if 0 < arr[i] <= n:
#             vis[arr[i] - 1] = True
#
#     print(vis)
#     # Find the first element which is unvisited
#     # in the original array
#     for i in range(1, n + 1):
#         if not vis[i - 1]:
#             return i
#
#     # if all elements from 1 to n are visited
#     # then n+1 will be first positive missing number
#     return n + 1
#
# if __name__ == "__main__":
#     arr = [2, -3, 4, 1, 1, 7]
#     print(missingNumber(arr))

# 33333333333333333333333333333

def missingNumber(arr):
    n = len(arr)
    for i in range(n):

        # if arr[i] is within the range 1 to n
        # and arr[i] is not placed at (arr[i]-1)th index in arr
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
            print("i", i)
            # then swap arr[i] and arr[arr[i]-1] to place arr[i]
            # to its corresponding index
            temp = arr[i]
            print("temp", temp)
            arr[i] = arr[arr[i] - 1]
            print("arr[i]", arr[i])
            arr[temp - 1] = temp
            print("first", arr)


    print(arr)

    # If any number is not at its corresponding index, then it
    # is the missing number
    for i in range(1, n + 1):
        if i != arr[i - 1]:
            return i

    # If all number from 1 to n are present
    # then n + 1 is smallest missing number
    return n + 1


if __name__ == '__main__':
    arr = [2, -3, 4, 1, 1, 7]
    print(missingNumber(arr))