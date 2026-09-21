# Given a circular array arr[], find the maximum sum of any non-empty subarray. A circular array allows wrapping from the end back to the beginning.
# Note: A subarray may wrap around the end and continue from the beginning, forming a circular segment.



# [Expected Approach] Using Kadane's Algorithm – O(n) Time and O(1) Space-------------------------------------------

def maxCircularSum(arr):

    totalSum = 0
    currMaxSum = 0
    currMinSum = 0
    maxSum = arr[0]
    minSum = arr[0]

    for i in range(len(arr)):

        # Kadane's to find maximum sum subarray
        currMaxSum = max(currMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxSum)

        # Kadane's to find minimum sum subarray
        currMinSum = min(currMinSum + arr[i], arr[i])
        minSum = min(minSum, currMinSum)

        # Sum of all the elements of input array
        totalSum += arr[i]

    normalSum = maxSum
    circularSum = totalSum - minSum

    # If the minimum subarray is equal to total Sum
    # then we just need to return normalSum
    if minSum == totalSum:
        return normalSum

    return max(normalSum, circularSum)


if __name__ == "__main__":

    arr = [8, -8, 9, -9, 10, -11, 12]

    print(maxCircularSum(arr))
