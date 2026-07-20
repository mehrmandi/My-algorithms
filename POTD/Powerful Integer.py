# import heapq

# def powerfulInteger(intervals, k):
#     n = len(intervals)
#     hash = {}
#     max_res = []
#     heapq.heapify(max_res)
    
    
#     for i in range(n):
#         j = intervals[i][0]
#         while j <= intervals[i][1]:
#             hash[j] = hash.get(j, 0) + 1
#             if hash[j] >= k:
#                 heapq.heappush(max_res, -j)
#             j += 1
            
#     if max_res:
#         return -max_res[0]
#     else:
#         return -1
            
    
    
# n = 5
# intervals = [[16, 21], [5, 8], [12, 17], [17, 29], [9, 24]]
# k = 3
# print(powerfulInteger(intervals, k))


# def powerfulInteger(intervals, k):
#     n = len(intervals)
#     comb = []
#     res = 0
#     count = 0

    
    
#     for i in range(n):
#         comb.append((intervals[i][0], False))
#         comb.append((intervals[i][1], True))
    
#     comb.sort()
        
#     for i in comb:
#         num , flag = i[0], i[1]
#         if not flag:
#             count += 1
            
#         if count >= k:
#             res = max(res, num)
              
#         if flag:
#             count -= 1
            
        
           
#     return res if res > 0 else -1
    

# intervals = [[1, 4], [12, 45], [3, 8], [10, 12]]
# k = 3
# print(powerfulInteger(intervals, k))

# [Expected Approach] Using Sweep Line - O(n log(n)) Time and O(n) Space-----------------------------
def powerfulInteger(intervals, k):
    mpp = {}

    # Mark interval start and
    # end+1 with +1 and -1 respectively
    for start, end in intervals:
        mpp[start] = mpp.get(start, 0) + 1
        mpp[end + 1] = mpp.get(end + 1, 0) - 1

    ans = -1
    temp = 0
    print(mpp, sorted(mpp))

    # Traverse the map (sorted keys) and
    # track frequency using prefix sum
    for point in sorted(mpp):
        delta = mpp[point]

        if delta >= 0:
            temp += delta
            if temp >= k:
                ans = point
        else:
            if temp >= k:
                ans = point - 1
            temp += delta

    return ans


if __name__ == "__main__":
    intervals = [[1, 4], [12, 45], [3, 8], [10, 12]]
    k = 3

    result = powerfulInteger(intervals, k)
    print(result)
