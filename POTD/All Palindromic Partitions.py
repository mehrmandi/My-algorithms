# Given a string s, find all possible ways to partition it such that every substring in the partition is a palindrome.

# Time Complexity: O(n² + 2n×n), (n2) time for precomputing palindromic substrings and O(2n × n) for backtracking through all partitions.
# Auxiliary Space: O(n2), for the DP table and O(n) for the recursion stack and temporary storage during backtracking.

# Precompute all palindromic substrings in s
def palindromes(s, dp):
    n = len(s)

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check two-character substrings
    for i in range(n - 1):
        dp[i][i + 1] = (s[i] == s[i + 1])

    # Check substrings of length 3 or more using bottom-up DP
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

# Recursive function to find all palindromic partitions


def backtrack(idx, s, curr, res, dp):
    # If we have reached the end of the string, store current partition
    if idx == len(s):
        res.append(list(curr))
        return

    # Try all substrings starting from index idx
    for i in range(idx, len(s)):
        # If s[idx..i] is a palindrome, we can include it
        if dp[idx][i]:
            # Choose the substring
            curr.append(s[idx:i + 1])
            # Explore further from next index
            backtrack(i + 1, s, curr, res, dp)
            # Undo the choice (backtrack)
            curr.pop()

# Return all palindromic partitions of string s


def palinParts(s):
    n = len(s)
    # DP table to store if substring s[i..j] is a palindrome
    dp = [[False] * n for _ in range(n)]

    # Precompute all palindromic substrings using DP
    palindromes(s, dp)

    # Final result
    res = []
    # Current partition
    curr = []
    # Begin backtracking from index 0
    backtrack(0, s, curr, res, dp)
    return res


if __name__ == "__main__":
    s = "geeks"

    # Get all palindromic partitions
    result = palinParts(s)

    # Print each valid partition
    for partition in result:
        print(" ".join(partition))
