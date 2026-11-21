# Given an integer x and an array of integers, arr[]. Find the length of the smallest subarray whose sum is strictly greater than x.

# If no such subarray exists, return 0.

# Sliding Window - O(n) Time and O(1) Space

def smallestSubWithSum(arr, x):
    n = len(arr)
    i = 0
    sum = 0
    ans = float('inf')

    # Expand the window
    for j in range(n):
        sum += arr[j]

        # Shrink the window while sum exceeds x
        while sum > x:
            ans = min(ans, j - i + 1)
            sum -= arr[i]
            i += 1

    # Return 0 if no valid subarray exists
    if ans == float('inf'):
        return 0

    return ans


x = 100
arr = [1, 10, 5, 2, 7]
print(smallestSubWithSum(arr, x))