def kadene(arr, dp, n):
    # Minimum sum of subarray ending at current position
    minEnding = arr[0]

    # Maximum sum of subarray ending at current position
    maxEnding = arr[0]

    for i in range(1, n):
        # Either extend the previous subarray or start
        # new from current element
        if minEnding + arr[i] < arr[i]:
            dp[i][0] = minEnding + arr[i]
            minEnding = minEnding + arr[i]
            
        else:
            minEnding = arr[i]
            
        if maxEnding + arr[i] > arr[i]:
            dp[i][1] = maxEnding + arr[i]
            maxEnding = maxEnding + arr[i]

        else:
            maxEnding = arr[i]
            
            
def kadene_reverse(arr, dp, n):
    res = max(abs(dp[n - 2][0] - arr[n - 1]), abs(dp[n - 2][1] - arr[n - 1]))
    
    # Minimum sum of subarray ending at current position
    minEnding = arr[n - 1]

    # Maximum sum of subarray ending at current position
    maxEnding = arr[n - 1]

    for i in range(n - 2 , 0, -1):
        # Either extend the previous subarray or start
        # new from current element
        if minEnding + arr[i] < arr[i]:
            minEnding = minEnding + arr[i]

        else:
            minEnding = arr[i]

        if maxEnding + arr[i] > arr[i]:
            maxEnding = maxEnding + arr[i]

        else:
            maxEnding = arr[i]
    
        res = max(res, max(abs(dp[i - 1][0] - maxEnding), abs(dp[i - 1][1] - minEnding)))
        
        
    return res
        


def maxDiffSubArrays(arr):
    n = len(arr)
    
    dp = [[arr[i], arr[i]] for i in range(n)]
    
    dp[0] = [arr[0], arr[0]]
    
    
    kadene(arr, dp, n)
    
    
    return kadene_reverse(arr, dp, n)
    
    
arr = [2, -1, -2, 1, -4, 2, 8]
print(maxDiffSubArrays(arr))
