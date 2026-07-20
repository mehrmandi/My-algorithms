from bisect import bisect_left, insort


# [Better Approach 2] Using Bottom-Up DP(Tabulation) - O(n2) Time and O(n) Space--------------------
# def maxSumIS(arr):
#     n = len(arr)
    
#     dp = [x for x in arr]
    
#     for i in range(n):
        
#         for j in range(i + 1, n):
#             if arr[j] > arr[i]:
#                 dp[j] = max(dp[i] + arr[j], dp[j])
             
#     return max(dp)
            

# arr = [5, 3, 2, 4, 7, 9, 8, 2, 3]
# print(maxSumIS(arr))

# [Expected Approach] Using Optimized Dynamic Programming - O(n log(n)) time and O(n) space--------------
def maxSumIS(arr):

    # key = value in arr, value = max sum ending
    # with that value or less than that value
    dp = {}
    keys = []
    ans = 0

    for val in arr:

        # Find the best sum among
        # all elements smaller than val
        idx = bisect_left(keys, val)
        bestSmaller = 0
        print(val, idx, dp)
        if idx > 0:
            bestSmaller = dp[keys[idx - 1]]
        print("bestsmaller", bestSmaller)

        currSum = bestSmaller + val

        # If this value gives a
        # better sum, update TreeMap
        if val not in dp or dp[val] < currSum:
            dp[val] = currSum
            if val not in keys:
                insort(keys, val)

            # Remove entries with greater
            # keys with smaller or equal sums
            i = bisect_left(keys, val) + 1
            while i < len(keys):
                if dp[keys[i]] <= currSum:
                    del dp[keys[i]]
                    keys.pop(i)
                else:
                    break

        ans = max(ans, currSum)

    return ans


if __name__ == "__main__":
    arr = [1, 101, 2, 3, 100]
    print(maxSumIS(arr))
