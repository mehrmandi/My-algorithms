import heapq
def isPossible(arr, k):
    n = len(arr)
    
    q = []
    i = 0
    
    while i < n:
        if not q:
            heapq.heappush(q, (arr[i], 1))
            i += 1
            
        else:
            top = q[0]
            if arr[i] == top[0]:
                heapq.heappush(q, (arr[i], 1))
                i += 1
            
            elif arr[i] == top[0] + 1:
                heapq.heappop(q)
                heapq.heappush(q, (arr[i], top[1] + 1))
                i += 1
                
            else:
                if top[1] < k:
                    return False
                heapq.heappop(q)
                
    
    while q:
        if q[0][1] < k:
            return False
        
        heapq.heappop(q)
        
    return True
        

arr = [8, 9, 10, 11, 11, 12, 13]
k = 2
print(isPossible(arr, k))
