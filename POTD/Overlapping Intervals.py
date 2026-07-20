

# def mergeOverlap(arr):
#     arr.sort()
#     n = len(arr)
#     left = arr[0][0]
#     right = arr[0][1]
    
#     res = []
    
#     for i in range(1, n):
#         new_left, new_right = arr[i]
        
#         if new_left > right:
#             res.append([left, right])
#             left = new_left
#             right = new_right
        
#         if new_left <= right:
#             if new_right > right:
#                 right = new_right
                
#     if [left, right] not in res:
#         res.append([left, right])
    
#     return res
    

# arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
# print(mergeOverlap(arr))
# [Expected Approach] Checking Last Merged Interval – O(n*log(n)) Time and O(n) Space--------------
def mergeOverlap(arr):

    # Sort intervals based on start values
    arr.sort()

    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res


if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    res = mergeOverlap(arr)

    for interval in res:
        print(interval[0], interval[1])
