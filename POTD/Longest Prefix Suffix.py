# # [Expected approach] Using LPS of KMP Algorithm
# # Time Complexity: O(n) we iterate through the string once using the i pointer, and in the worst case, each character is processed at most twice (once when matched, once when falling back via len = lps[len - 1]).
# # Auxiliary Space: O(n)

# def getLPSLength(s):
#     n = len(s)
#     j = 0
#     i = 1
#     lps = [0] * n

    
#     while i < n:
#         if s[i] == s[j]:
#             j += 1
#             lps[i] = j
#             i += 1
            
#         else:
#             if j != 0:
#                 j = lps[j - 1]
                
            
#             else:
#                 lps[i] = 0
#                 i += 1
        
        
#     return lps[n - 1]

# s = "aabcdaabc"
# print(getLPSLength(s))

#  [Efficient Approach] Double Hash Prefix-Suffix Check - O(n) Time and O(1) Space---------------------------------------------------
def getLPSLength(s):
    base1, base2 = 31, 37
    mod1, mod2 = int(1e9 + 7), int(1e9 + 9)

    p1 = p2 = 1
    n = len(s)

    # hash1 for prefix, hash2 for suffix
    hash1 = [0, 0]
    hash2 = [0, 0]
    ans = 0

    for i in range(n - 1):

        # Update prefix hashes
        hash1[0] = (hash1[0] + (ord(s[i]) -
                                ord('a') + 1) * p1) % mod1
        hash1[1] = (hash1[1] + (ord(s[i]) -
                                ord('a') + 1) * p2) % mod2

        # Update suffix hashes
        hash2[0] = (hash2[0] * base1 +
                    (ord(s[n - i - 1]) - ord('a') + 1)) % mod1
        hash2[1] = (hash2[1] * base2 +
                    (ord(s[n - i - 1]) - ord('a') + 1)) % mod2

        # Check if both hash pairs match
        if hash1 == hash2:
            ans = i + 1

        # Update powers
        p1 = (p1 * base1) % mod1
        p2 = (p2 * base2) % mod2

    return ans


if __name__ == "__main__":
    s = "ababab"
    print(getLPSLength(s))
