import heapq
# [Expected Approach] Greedy with Heap - O(n*log(n)) Time and O(n) Space----------------------------------------
def minCost(arr):
    arr.sort()
    q = [x for x in arr]
    heapq.heapify(q)
    res = 0

    while q:
        if len(q) == 1:
            return res
        
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        new_num = first + second
        res += new_num
        heapq.heappush(q, new_num)
            

    return res
            
    
arr = [4, 2, 7, 6, 9]
print(minCost(arr))
