def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def substringCheck(s):
    n = len(s)
    hash = {}
    hash2 = {}
    
    for i in range(n):
        if s[i] not in hash:
            hash[s[i]] = 1
        else:
            if s[i] not in hash2:
                hash2[s[i]] = 2
            else:
                hash2[s[i]] += 1
    
    res = n
    
    for key, val in hash2.items():
        add = factorial(val) // (factorial(val - 2) * 2)
        res += add
        
    return res


# [Expected Approach] Using Character Frequency - O(n) time and O(1) space---------------------
# Python program to count all substrings with same
# first and last characters.

# def substringCheck(s):
#     n = len(s)

#     # Create an array to store
#     # frequency of characters
#     freq = [0] * 26

#     # Update frequency of each character
#     for i in range(n):
#         freq[ord(s[i]) - ord('a')] += 1

#     count = 0

#     # For each character, calculate number of substrings
#     # that start and end with that character
#     for i in range(26):

#         # Number of substrings with same
#         # first and last character is
#         # nC2 + n = n*(n+1)/2
#         count += (freq[i] * (freq[i] + 1)) // 2

#     return count




# [Naive Approach] Using Two Nested Loops - O(n^2) time and O(1) space-----------------------
# Python program to count all substrings with same
# first and last characters.

# def substringCheck(s):
#     count = 0
#     n = len(s)

#     # Consider all possible substrings
#     for i in range(n):
#         for j in range(i, n):

#             # If first and last characters
#             # of substring s[i..j] are same
#             if s[i] == s[j]:
#                 count += 1

#     return count



s = "aabacdabb"
print(substringCheck(s))
