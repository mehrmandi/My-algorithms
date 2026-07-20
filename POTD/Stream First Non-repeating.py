def firstNonRepeating(s):
    n = len(s)
    res = ""
    res += s[0]
    hash = {s[0]:1}
    non_rep_idx = 0

    
    for i in range(1, n):
        if s[i] not in hash:
            hash[s[i]] = 1
            res += s[non_rep_idx]
        else:
            if non_rep_idx <= i:
                hash[s[i]] += 1
                while hash[s[non_rep_idx]] > 1 and non_rep_idx < i:
                    non_rep_idx += 1
                
                if non_rep_idx == i:
                    res += "#"
                    non_rep_idx += 1
                else:
                    res += s[non_rep_idx]
                    
    return res

# [Better Approach] Using Queue and Frequency Array - O(n) Time and O(n) Space------------------------


           
# from collections import deque


# def firstNonRepeating(s):
#     ans = ""
#     count = [0] * 26
#     q = deque()

#     for char in s:

#         # if non-repeating element found push it in queue
#         if count[ord(char) - ord('a')] == 0:
#             q.append(char)
#         count[ord(char) - ord('a')] += 1

#         # if front element is repeating pop it from the queue
#         while q and count[ord(q[0]) - ord('a')] > 1:
#             q.popleft()

#         # if queue is not empty append front
#         # element else append "#" in ans string.
#         if q:
#             ans += q[0]
#         else:
#             ans += '#'

#     return ans

# [Expected Approach] Using Frequency and Last Occurrence Array - O(n) Time and O(1) Space-------------------

def firstNonRepeating(s):
    n = len(s)
    freq = [0] * 26
    firstPos = [-1] * 26

    # record first occurrence for each character
    for i in range(n):
        if firstPos[ord(s[i]) - ord('a')] == -1:
            firstPos[ord(s[i]) - ord('a')] = i

    result = ""
    for i in range(n):
        freq[ord(s[i]) - ord('a')] += 1

        chosen = '#'
        earliest = n + 1

        # find earliest character with frequency 1
        for j in range(26):
            if freq[j] == 1 and earliest > firstPos[j]:
                chosen = chr(j + ord('a'))
                earliest = firstPos[j]
        result += chosen

    return result
s = "bcbdaana"
# bbcccccc
print(firstNonRepeating(s))
    
