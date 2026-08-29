# Given a numeric string s containing only digits and an integer n, count the number of non-empty subsequences of s whose numeric value is divisible by n. Return the answer modulo 1e9 + 7.

# Space Optimized Approach - O(n * m) Time and O(n) Space
def countSubsequences(s, n):

    MOD = 10**9 + 7

    # dp[rem] stores the number of subsequences
    # having remainder rem modulo n.
    dp = [0] * n

    # Process each digit of the string.
    for ch in s:

        digit = int(ch)

        # Copy the previous DP state.
        curr = dp[:]

        # Start a new subsequence with the current digit.
        curr[digit % n] = (curr[digit % n] + 1) % MOD

        # Append the current digit to all existing subsequences.
        for rem in range(n):
            newRem = (rem * 10 + digit) % n
            curr[newRem] = (curr[newRem] + dp[rem]) % MOD

        # Move to the next digit.
        dp = curr

    return dp[0]


s = "1234"
n = 4
print(countSubsequences(s, n))
