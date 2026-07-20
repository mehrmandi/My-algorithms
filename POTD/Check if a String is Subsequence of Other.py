# def isSubSeq(s1, s2):
#     n = len(s1)
#     m = len(s2)
#     first, sec = 0, 0
    
#     while first < n and sec < m:
#         while s1[first] != s2[sec]:
#             if sec < m:
#                 sec += 1
#             if sec == m:
#                 return False
        
#         if first == n - 1:
#             return True
        
#         first += 1
#         sec += 1
        
            

# s1 = "gksrek"
# s2 = "geeksfogeekrs"
# print(isSubSeq(s1, s2))

# Time Complexity: O(n)
# Auxiliary Space: O(1)
def issubsequence(s1, s2):

    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1

    # If i reaches end of s1,that mean we found all
    # characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n


if __name__ == "__main__":
    s1 = "gksrek"
    s2 = "geeksforgeeks"
    if (issubsequence(s1, s2)):
        print("true")
    else:
        print("false")
