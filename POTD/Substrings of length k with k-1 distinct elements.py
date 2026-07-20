def substringDistinctElement(s, k):
    n = len(s)
    if n < k:
        return -1

    left, right = 0, k

    window = s[left:right]
    need_distinct = len(set(window)) - k + 1
    count = 1 if need_distinct == 0 else 0
    char_count = {char: window.count(char) for char in set(window)}

    

    while right < n:    
        char_count[s[left]] -= 1
        if char_count[s[left]] == 0:
            need_distinct -= 1
            char_count.pop(s[left])
            
        if s[right] in char_count:
            char_count[s[right]] += 1
            
        if s[right] not in char_count:
            need_distinct += 1
            char_count[s[right]] = 1
        
        if need_distinct == 0:  
            count += 1

        left += 1
        right += 1
    
        
    return count     


s = "aabab"
k = 3
print(substringDistinctElement(s, k))


# def substrCount(s, k):

#     if k > len(s):
#         return 0

#     n = len(s)
#     cnt = [0] * 26
#     ans = 0

#     for i in range(k - 1):
#         cnt[ord(s[i]) - ord('a')] += 1

#     for i in range(k - 1, n):

#         cnt[ord(s[i]) - ord('a')] += 1

#         # Check if the current window
#         # contains k-1 distinct chars.
#         distinctCnt = sum(1 for x in cnt if x > 0)
#         if distinctCnt == k - 1:
#             ans += 1

#         cnt[ord(s[i - k + 1]) - ord('a')] -= 1

#     return ans


# if __name__ == "__main__":
#     s = "aabab"
#     k = 3
#     print(substrCount(s, k))
