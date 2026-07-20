# def max_min_pair_sum(arr):
#     n = len(arr)
#     max_sum = float('-inf')

#     for i in range(n):
#         for j in range(i + 1, n):
#             sub = arr[i:j + 1]
#             if len(sub) >= 2:
#                 # Get two smallest elements efficiently
#                 first = second = float('inf')
#                 for num in sub:
#                     if num < first:
#                         second = first
#                         first = num
#                     elif num < second:
#                         second = num
#                 max_sum = max(max_sum, first + second)

#     return max_sum


# # Example usage
# arr = [4, 3, 5, 1]
# print(max_min_pair_sum(arr))  # Output: 8


# def max_min_pair_sum(arr):
#     n = len(arr)
#     max_sum = float('-inf')

#     # Iterate through adjacent pairs
#     for i in range(n - 1):
#         a, b = arr[i], arr[i + 1]
#         min1, min2 = min(a, b), max(a, b)
#         max_sum = max(max_sum, min1 + min2)

#     # Optionally scan longer windows
#     stack = []
#     for num in arr:
#         while stack and stack[-1] > num:
#             stack.pop()
#         if stack:
#             max_sum = max(max_sum, num + stack[-1])
#         stack.append(num)

#     return max_sum


# # Example usage
# arr = [4, 3, 5, 1]
# print(max_min_pair_sum(arr))  # Output: 8


# [Expected Approach] By maximizing consecutive element sum - O(n) Time and O(1) Space


def maxSum(arr):
    n = len(arr)

    # find two consecutive elements with maximum sum
    res = arr[0] + arr[1]
    for i in range(1, n - 1):
        res = max(res, arr[i] + arr[i + 1])

    return res


if __name__ == "__main__":
    arr = [5, 4, 3, 1, 6]
    print(maxSum(arr))
