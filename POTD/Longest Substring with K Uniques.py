def longestKSubstring(s, k):
    n = len(s)
    if n < k:
        return -1
    
    char_count = {}
    max_len = -1
    left, right = 0, 0

    
    
    while right < n:
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            
            left += 1
        
        if len(char_count) == k:    
            max_len = max(max_len, right - left + 1)
            
        right += 1
                 
    return max_len

        
s = "aabaaab"
k = 2
print(longestKSubstring(s, k))


# [Expected Approach]Sliding Window with Frequency Count - O(n) Time and O(1) Space


# def longestKSubstr(s, k):
#     n = len(s)
#     i = 0
#     j = 0
#     cnt = 0
#     maxi = -1
#     fre = [0] * 26

#     # cnt represents the number of
#     # unique characters in the current window

#     while j < n:

#         # include s[j] into the window
#         fre[ord(s[j]) - ord('a')] += 1

#         # it is the first occurrence of
#         # this character in the window
#         if fre[ord(s[j]) - ord('a')] == 1:
#             cnt += 1

#         # shrink the window if the number of
#         # unique character is more than k
#         while cnt > k:
#             fre[ord(s[i]) - ord('a')] -= 1

#             # one unique character removed
#             if fre[ord(s[i]) - ord('a')] == 0:
#                 cnt -= 1
#             i += 1

#         # we have exactly k unique characters
#         if cnt == k:
#             maxi = max(maxi, j - i + 1)

#         j += 1

#     return maxi


# if __name__ == "__main__":
#     s = "aabacbebebe"
#     k = 3
#     print(longestKSubstr(s, k))
