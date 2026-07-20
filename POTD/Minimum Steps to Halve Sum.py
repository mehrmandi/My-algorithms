import heapq

def minOperations(arr):
    sum_arr = sum(arr)
    target = sum_arr / 2
    res = 0
    q = []
    
    for num in arr:
        heapq.heappush(q, -num)
        
    
    while sum_arr > target:
        half_num = heapq.heappop(q)
        sum_arr += half_num / 2
        heapq.heappush(q, half_num / 2)
        res += 1
    
    
    return res


arr = [8, 6, 2]
print(minOperations(arr))
