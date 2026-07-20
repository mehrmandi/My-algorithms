import heapq
import math

# [Expected Approach - 1] Using Sorting - O(n log(n)) Time and O(n) Space-------------------------------------
# def minSoldiers(arr, k):
#     n = len(arr)
#     needing = [0 for _ in range(n)]
#     luck = math.ceil(n/2)
    
    
#     for i in range(n):
#         residual = arr[i] % k
#         if residual != 0:
#             needing[i] = k - (arr[i] % k)
    
        
#     needing.sort()
    
#     return sum(needing[:luck])
        
        
# arr = [3, 5, 6, 7, 9, 10]
# k = 9
# print(minSoldiers(arr, k))


# Time Complexity: O(n + m * log(m)), where m is the number of unlucky troops (at most n).--------------------------------
# Auxiliary Space: O(m)

def minSoldiers(arr, k):
    n = len(arr)
    need = (n + 1) // 2
    lucky = 0

    # Min-heap for storing costs to make a troop lucky
    pq = []

    for num in arr:
        if num % k == 0:
            lucky += 1
        else:
            heapq.heappush(pq, k - (num % k))

    # If already enough lucky troops, cost is 0
    if lucky >= need:
        return 0

    total = 0
    required = need - lucky

    # Take smallest `required` costs from heap
    for _ in range(required):
        if pq:
            total += heapq.heappop(pq)

    return total


if __name__ == "__main__":
    arr = [3, 5, 6, 7, 9, 11]
    k = 4
    print(minSoldiers(arr, k))
