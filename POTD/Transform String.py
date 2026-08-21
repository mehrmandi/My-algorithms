# Given two strings s1 and s2. Find the minimum number of steps required to transform string s1 into string s2. The only allowed operation for the transformation is selecting a character from string s1 and inserting it in the beginning of string s1.

# If transformation is not possible return -1.

# Using Counter and Two Pointers - O(n) Time and O(k) Space, where k is the number of unique characters in the strings.

from collections import Counter


def transform(s1, s2):
    if len(s1) != len(s2):
        return -1

    if Counter(s1) != Counter(s2):
        return -1

    i = j = len(s1) - 1
    res = 0

    while i >= 0:
        if s1[i] == s2[j]:
            i -= 1
            j -= 1
        else:
            res += 1
            i -= 1

    return res
    

s1 = "EACBD"
s2 = "EABCD"
print(transform(s1, s2))

    
        
    
    