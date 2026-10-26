# You are given an array arr[] of size n. You need to remove a subarray of size k, such that the difference between the maximum and minimum values of the remaining array is minimized. Find the minimum value obtained after performing the operation of the removal of the subarray.

# Suffix Preprocessing and Prefix Tracking - O(n) Time and O(n) Space


def minDiff(k, arr):

    n = len(arr)

    # Maximum and minimum values from each index to the end.
    suffixMax = [0] * n
    suffixMin = [0] * n

    suffixMax[n - 1] = arr[n - 1]
    suffixMin[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffixMax[i] = max(arr[i], suffixMax[i + 1])
        suffixMin[i] = min(arr[i], suffixMin[i + 1])

    # Remove the prefix of size k.
    res = suffixMax[k] - suffixMin[k]

    prefixMax = arr[0]
    prefixMin = arr[0]

    # Remove a middle subarray of size k.
    for i in range(1, n - k):

        currentMax = max(prefixMax, suffixMax[i + k])
        currentMin = min(prefixMin, suffixMin[i + k])

        res = min(res, currentMax - currentMin)

        prefixMax = max(prefixMax, arr[i])
        prefixMin = min(prefixMin, arr[i])

    # Remove the suffix of size k.
    res = min(res, prefixMax - prefixMin)

    return res


        
arr = [1, 2, 3, 4, 5]
k = 3
print(minDiff(k, arr))
