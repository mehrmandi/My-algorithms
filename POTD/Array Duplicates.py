# def findDuplicates(arr):
#     hash = {}
#     res = []
    
#     for num in arr:
#         if num not in hash:
#             hash[num] = 1
#         else:
#             res.append(num)

#     return res

# arr = [2, 3, 1, 2, 3]
# print(findDuplicates(arr))

# [Expected Approach] Negative Marking approach - O(n) Time and O(1) Space-----------
def findDuplicates(arr):

    ans = []

    for i in range(len(arr)):

        # convert value to index (1-based to 0-based)
        idx = abs(arr[i]) - 1

        # if already visited, it's a duplicate
        if arr[idx] < 0:
            ans.append(abs(arr[i]))
        else:

            # mark as visited
            arr[idx] = -arr[idx]

    return ans


if __name__ == "__main__":
    arr = [2, 3, 1, 2, 3]
    res = findDuplicates(arr)
    print(*res)
    
