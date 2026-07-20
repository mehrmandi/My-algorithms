def totalElements(arr):
    n = len(arr)
    hash = {arr[0]:1}
    max_len = 1
    dist = 1
    left = 0
    
    for i in range(1, n):
        if arr[i] in hash:
            hash[arr[i]] += 1
            
        else:
            hash[arr[i]] = 1
            dist += 1
            while dist > 2:
                hash[arr[left]] -= 1
                if hash[arr[left]] == 0:
                   dist -= 1
                   hash.pop(arr[left])
                   
                left += 1
        max_len = max(max_len, i - left + 1)
            
    return max_len       
                    
        
arr = [1, 2, 3, 3, 3, 6, 8, 8, 2, 2, 2]
print(totalElements(arr))


# [Expected Approach] Using Sliding Window - O(n) Time and O(1) Space


# def totalElements(arr):

#     # keeps frequency of elements
#     # in the current window
#     mp = {}
#     i = j = 0
#     n = len(arr)
#     size = 0

#     while j < n:

#         # Add the current element
#         # to the map (or update its count)
#         mp[arr[j]] = mp.get(arr[j], 0) + 1

#         # If we have more than 2 distinct elements
#         # shrink from the left
#         while len(mp) > 2:
#             mp[arr[i]] -= 1

#             # Remove the number completely
#             # if its count becomes 0
#             if mp[arr[i]] == 0:
#                 del mp[arr[i]]
#             i += 1

#         # update the longest size found so far
#         size = max(size, j - i + 1)
#         j += 1

#     return size


# if __name__ == "__main__":
#     arr = [0, 1, 2, 2, 2, 2]
#     print(totalElements(arr))





# def totalElements(arr):
#     n = len(arr)
#     cnt = [0] * (max(arr) + 1)
#     max_len = 0
#     left = 0

    
#     for i in range(n):
#         cnt[arr[i]] += 1
        
#         distinct = sum(1 for x in cnt if x > 0)
        
#         if distinct <= 2:
#             max_len = max(max_len, i - left + 1)
            
#         else:
#             cnt[arr[left]] -= 1
#             left += 1
            
            
#     return max_len
            

# arr = [2, 2, 2, 2, 2, 2]
# print(totalElements(arr))
