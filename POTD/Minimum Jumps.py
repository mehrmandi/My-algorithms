def minJump(arr):
    n = len(arr)
    dp = [float('inf') for _ in range(n)]

    for i in range(n):
        dp[0] = 0
        for j in range(arr[i] + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + 1)

    if dp[n - 1] == float('inf'):
        return -1
    else:
        return dp[n - 1]



arr = [9, 10, 1, 2, 3, 4, 8, 0, 0, 0, 0, 0, 0, 0, 1]

print(minJump(arr))