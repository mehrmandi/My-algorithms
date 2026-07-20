# [Expected Approach] Using Kadane's Algorithm – O(n) Time and O(1) Space-------------------------------------------


def kadane(arr):
    max_ending = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far


def max_circular_subarray(arr):
    max_kadane = kadane(arr)
    total_sum = sum(arr)
    inverted_arr = [-x for x in arr]
    min_subarray_sum = kadane(inverted_arr)
    circular_max = total_sum + min_subarray_sum  # because we negated the array

    # Edge case: all elements are negative
    if circular_max == 0:
        return max_kadane
    
    return max(max_kadane, circular_max)


# arr = [10, -3, -4, 7, 6, 5, -4, -1]  # [10, -3, -4, 7, 6, 5, -4, -1]
arr = arr = [14, -49, 25, 39, 41, -22, 30, -37, -14, -28, -43, 19, 0, 28, 43, -18, 16, 21, 42, -27, -20, -19, 29, 21, 30, 29, -25, 23, 2, -2]
# 270
print(max_circular_subarray(arr))


# [Expected Approach] Using Kadane's Algorithm – O(n) Time and O(1) Space-------------------------------------------

# def maxCircularSum(arr):

#     totalSum = 0
#     currMaxSum = 0
#     currMinSum = 0
#     maxSum = arr[0]
#     minSum = arr[0]

#     for i in range(len(arr)):

#         # Kadane's to find maximum sum subarray
#         currMaxSum = max(currMaxSum + arr[i], arr[i])
#         maxSum = max(maxSum, currMaxSum)

#         # Kadane's to find minimum sum subarray
#         currMinSum = min(currMinSum + arr[i], arr[i])
#         minSum = min(minSum, currMinSum)

#         # Sum of all the elements of input array
#         totalSum += arr[i]

#     normalSum = maxSum
#     circularSum = totalSum - minSum

#     # If the minimum subarray is equal to total Sum
#     # then we just need to return normalSum
#     if minSum == totalSum:
#         return normalSum

#     return max(normalSum, circularSum)


# if __name__ == "__main__":

#     arr = [8, -8, 9, -9, 10, -11, 12]

#     print(maxCircularSum(arr))
