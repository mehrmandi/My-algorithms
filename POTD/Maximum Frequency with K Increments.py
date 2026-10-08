
def maxFrequency(arr, k):
    # Sort the array to apply the sliding window.
    arr.sort()

    window_sum = 0
    left = 0
    res = 1

    for right in range(len(arr)):
        window_sum += arr[right]

        # Shrink the window if more than k increments are required.
        while arr[right] * (right - left + 1) - window_sum > k:
            window_sum -= arr[left]
            left += 1

        res = max(res, right - left + 1)

    return res


arr = [1, 2, 2, 4, 5, 5, 6]
k = 4
print(maxFrequency(arr, k))
