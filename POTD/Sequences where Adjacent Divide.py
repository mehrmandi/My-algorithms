# DP with Precomputed Factors and Multiples - O(n * m * logm) Time and (n * m) Space

def count(n, m):
    mod = 10**9 + 7

    # dp[len][val]
    # Number of valid arrays of length len
    # ending with value val
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # factors[x]  -> all factors of x
    # multiples[x] -> all multiples of x
    factors = [[] for _ in range(m + 1)]
    multiples = [[] for _ in range(m + 1)]

    # Precompute factors and multiples
    for i in range(1, m + 1):

        for j in range(i, m + 1, i):

            factors[j].append(i)

            # Avoid duplicate insertion
            if j != i:
                multiples[i].append(j)

    # Base Case:
    # Arrays of length 1
    for val in range(1, m + 1):
        dp[1][val] = 1

    # Build DP table
    for length in range(2, n + 1):

        for curr in range(1, m + 1):

            # Add all factors
            for prev in factors[curr]:

                dp[length][curr] = (dp[length][curr] +
                                    dp[length - 1][prev]) % mod

            # Add all multiples
            for prev in multiples[curr]:

                dp[length][curr] = (dp[length][curr] +
                                    dp[length - 1][prev]) % mod

    # Final Answer
    ans = 0

    for val in range(1, m + 1):
        ans = (ans + dp[n][val]) % mod

    return ans
    
    

m = 3
n = 3
print(count(n, m))  # Output: 220