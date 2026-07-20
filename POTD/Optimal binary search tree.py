# [Expected Approach 2] Using Bottom - Up Dp(Tabulation) - O(n ^ 3) Time and O(n ^ 2) Space-----------------------------------------


def sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s

# Function to calculate minimum cost of a Binary Search Tree using DP (tabulation)


def minCost(keys, freq):
    n = len(keys)

    # Create a 2D DP table to store minimum costs for subarrays of keys
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case: cost of a single key is its frequency
    for i in range(n):
        dp[i][i] = freq[i]

    # Consider chains of length 2 to n
    for l in range(2, n + 1):
        for i in range(0, n - l + 1):

            # j is the ending index of the chain
            j = i + l - 1
            dp[i][j] = float('inf')

            # Total frequency sum of keys in current range
            fsum = sum(freq, i, j)

            # Try each key in range [i..j] as root
            for r in range(i, j + 1):

                # Cost when keys[r] is root:
                # cost of left subtree + cost of right subtree + sum of frequencies
                c = (dp[i][r - 1] if r > i else 0) + \
                    (dp[r + 1][j] if r < j else 0) + fsum

                # Update minimum cost
                if c < dp[i][j]:
                    dp[i][j] = c

    # dp[0][n-1] stores minimum cost for all keys
    return dp[0][n - 1]


if __name__ == '__main__':
    keys = [10, 12, 20]
    freq = [34, 8, 50]

    print(minCost(keys, freq))

        
    
    
    
    
    
keys = [10, 12, 20]
freq = [34, 8, 50]
print(minCost(keys, freq))
