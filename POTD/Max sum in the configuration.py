def maxSum(arr):
    n = len(arr)

    # Compute sum of all array elements
    curSum = 0
    for i in range(n):
        curSum += arr[i]

    # Compute sum of i*arr[i] for initial
    # configuration.
    currVal = 0
    for i in range(n):
        currVal += i * arr[i]

    # Initialize result
    res = currVal

    # Compute values for other iterations
    for i in range(1, n):

        # Compute next value using previous
        nextVal = currVal - (curSum - arr[i - 1]) \
            + arr[i - 1] * (n - 1)

        # Update current value
        currVal = nextVal

        # Update result if required
        res = max(res, nextVal)

    return res



arr = [4, 5, 1, 2, 8]
print(maxSum(arr))