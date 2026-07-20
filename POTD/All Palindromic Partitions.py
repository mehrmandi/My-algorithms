# Time Complexity: O(n² × 2n), for exploring all possible partitions (2n) and checking each substring for palindrome in O(n) time.
# Auxiliary Space: O(n × 2n), for storing all palindromic partitions and using recursion stack up to depth n.


# Check if the string is a palindrome
# def isPalindrome(s):
#     return s == s[::-1]

# # Backtracking function to generate all palindromic partitions


# def backtrack(idx, s, curr, res):
#     if idx == len(s):
#         # Save the current valid partition
#         res.append(curr[:])
#         return

#     temp = ""
#     for i in range(idx, len(s)):
#         temp += s[i]
#         if isPalindrome(temp):
#             # Choose substring
#             curr.append(temp)
#             # Explore further
#             backtrack(i + 1, s, curr, res)
#             # Backtrack
#             curr.pop()

# # Generate all palindromic partitions and sort them


# def palinParts(s):
#     res = []
#     backtrack(0, s, [], res)
#     return res


# if __name__ == "__main__":
#     s = "geeks"
#     res = palinParts(s)
#     for part in res:
#         print(" ".join(part))


# ------------------------------------------------------------------------------------


# def is_palindrome(s):
#     return s == s[::-1]


# def partition_palindromes(s):
#     result = []

#     def backtrack(start, path):
#         if start == len(s):
#             result.append(path[:])
#             return
#         for end in range(start + 1, len(s) + 1):
#             substr = s[start:end]
#             if is_palindrome(substr):
#                 path.append(substr)
#                 backtrack(end, path)
#                 path.pop()

#     backtrack(0, [])
#     return result

# s = "geeks"
# print(partition_palindromes(s))


#  Time Complexity: O(n² × 2n) for generating all possible partitions (2n) and checking each partition for palindromes (up to O(n2) per partition).
# Auxiliary Space: O(n × 2n), to store all palindromic partitions, each potentially having up to n substrings.

# Stores all valid palindromic partitions
# ans = []

# Check if all substrings in the partition are palindromes


# def isAllPalindromes(partition):
#     for s in partition:
#         i, j = 0, len(s) - 1
#         while i < j:
#             if s[i] != s[j]:
#                 return False
#             i += 1
#             j -= 1
#     return True

# # Generate partition of string based on the binary cut pattern


# def createPartition(s, cutPattern):
#     currentPartition = []
#     subStr = s[0]

#     for i in range(len(cutPattern)):
#         # If no cut, append next character to current substring
#         if cutPattern[i] == '0':
#             subStr += s[i + 1]
#         # If cut, push current substring and start a new one
#         else:
#             currentPartition.append(subStr)
#             subStr = s[i + 1]

#     # Push the last substring
#     currentPartition.append(subStr)

#     # Store partition if all substrings are palindromes
#     if isAllPalindromes(currentPartition):
#         ans.append(currentPartition)

# # Recursively generate all cut patterns (bit strings)


# def generateCut(s, cutPattern):
#     # When pattern is complete, create partition
#     if len(cutPattern) == len(s) - 1:
#         createPartition(s, cutPattern)
#         return

#     # Try with a cut
#     generateCut(s, cutPattern + '1')

#     # Try without a cut
#     generateCut(s, cutPattern + '0')

# # Generate all palindromic partitions of the string


# def palinParts(s):
#     generateCut(s, "")
#     return ans


# if __name__ == "__main__":
#     s = "geeks"
#     result = palinParts(s)
#     for partition in result:
#         print(" ".join(partition))


# Time Complexity: O(n² + 2n×n), (n2) time for precomputing palindromic substrings and O(2n × n) for backtracking through all partitions.
# Auxiliary Space: O(n2), for the DP table and O(n) for the recursion stack and temporary storage during backtracking.
# Precompute all palindromic substrings in s
# def palindromes(s, dp):
#     n = len(s)

#     # All single characters are palindromes
#     for i in range(n):
#         dp[i][i] = True

#     # Check two-character substrings
#     for i in range(n - 1):
#         dp[i][i + 1] = (s[i] == s[i + 1])

#     # Check substrings of length 3 or more using bottom-up DP
#     for length in range(3, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1
#             dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

# # Recursive function to find all palindromic partitions


# def backtrack(idx, s, curr, res, dp):
#     # If we have reached the end of the string, store current partition
#     if idx == len(s):
#         res.append(list(curr))
#         return

#     # Try all substrings starting from index idx
#     for i in range(idx, len(s)):
#         # If s[idx..i] is a palindrome, we can include it
#         if dp[idx][i]:
#             # Choose the substring
#             curr.append(s[idx:i + 1])
#             # Explore further from next index
#             backtrack(i + 1, s, curr, res, dp)
#             # Undo the choice (backtrack)
#             curr.pop()

# # Return all palindromic partitions of string s


# def palinParts(s):
#     n = len(s)
#     # DP table to store if substring s[i..j] is a palindrome
#     dp = [[False] * n for _ in range(n)]

#     # Precompute all palindromic substrings using DP
#     palindromes(s, dp)

#     # Final result
#     res = []
#     # Current partition
#     curr = []
#     # Begin backtracking from index 0
#     backtrack(0, s, curr, res, dp)
#     return res


# if __name__ == "__main__":
#     s = "geeks"

#     # Get all palindromic partitions
#     result = palinParts(s)

#     # Print each valid partition
#     for partition in result:
#         print(" ".join(partition))
