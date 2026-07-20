# Python Implementation for Largest Divisible Subset
# using Recursion
# def lds(res, curr, i, prev, arr):
#     # Base case: check if we've reached the
#     # end of the array
#     if i >= len(arr):
#         # Update res if the current subset is
#         # larger or if it's the same size but lexicographically greater
#         if len(curr) > len(res) or (len(curr) == len(res) and curr > res):
#             res[:] = curr[:]
#         return

#     # Include current element if divisible by
#     # previous element
#     if not curr or arr[i] % prev == 0:
#         curr.append(arr[i])

#         # Recur with the current number included
#         lds(res, curr, i + 1, arr[i], arr)

#         # Backtrack to explore other possibilities
#         curr.pop()

#     # Exclude current element and move to the next
#     # Recur without including the current number
#     lds(res, curr, i + 1, prev, arr)

# # Main function to find the largest divisible subset


# def largestSubset(arr):
#     arr.sort()
#     res = []
#     curr = []

#     # Start the recursive search
#     lds(res, curr, 0, 1, arr)
#     return res


# if __name__ == "__main__":
#     arr = [1, 16, 7, 8, 4]

#     res = largestSubset(arr)

#     for num in res:
#         print(num, end=" ")

# [Expected Approach 1] Using Top-Down DP(Memoization) - O(n^2) Time and O(n) Space----------------------------------------
# def lds(arr, memo, parent, i):
#     # If this subproblem has already been solved, return the result
#     if memo[i] != -1:
#         return memo[i]

#     maxLength = 1
#     bestParent = -1

#     # Try to include arr[i] in the subset by checking all j < i
#     for j in range(i):
#         # Adjusted for descending order
#         if arr[j] % arr[i] == 0:
#             length = lds(arr, memo, parent, j) + 1
#             if length > maxLength:
#                 maxLength = length
#                 bestParent = j

#     # Store the result for memoization and backtracking
#     memo[i] = maxLength
#     parent[i] = bestParent
#     return maxLength

# # Main function to find the largest divisible subset


# def largestSubset(arr):
#     n = len(arr)

#     # Sort in descending order
#     arr.sort(reverse=True)

#     # Memoization array
#     memo = [-1] * n
#     # Backtracking parent array
#     parent = [-1] * n

#     maxSize = 0
#     lastIndex = 0

#     # Try to find the largest subset size for each index
#     for i in range(n):
#         size = lds(arr, memo, parent, i)
#         if size > maxSize:
#             maxSize = size
#             lastIndex = i

#     # Backtrack to construct the result
#     res = []
#     while lastIndex != -1:
#         res.append(arr[lastIndex])
#         lastIndex = parent[lastIndex]

#     # Already in descending order due to backtracking
#     return res

# [Expected Approach 2] Using Bottom-Up DP (Tabulation) – O(n^2) Time and O(n) Space--------------------------------------
def largestSubset(arr):

    arr.sort(reverse=True)
    n = len(arr)

    # Table to store the size of
    # largest subset
    dp = [1] * n

    # To keep track of previous elements
    parent = [-1] * n

    # Fill dp table
    max_size = 1
    last_index = 0

    for i in range(1, n):
        for j in range(i):
            if arr[j] % arr[i] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j

        # Update max_size and last_index
        if dp[i] > max_size:
            max_size = dp[i]
            last_index = i

    # Backtrack to construct the subset
    res = []
    while last_index >= 0:
        res.append(arr[last_index])
        last_index = parent[last_index]

    # Reverse the result to get it
    # in correct order
    return res


if __name__ == "__main__":

    arr = [1, 16, 7, 8, 4]

    res = largestSubset(arr)
    for num in res:
        print(num, end=" ")
