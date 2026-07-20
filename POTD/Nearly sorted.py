import heapq

def nearlySorted(arr, k):
    n = len(arr)
    q = []
    
    for i in range(k):
        heapq.heappush(q, arr[i])
        
    idx = 0
    i = k
    
    while i < n:
        heapq.heappush(q, arr[i])
        print(q)
        
        arr[idx] = heapq.heappop(q)
        
        i += 1
        idx += 1
        
    while q:
        arr[idx] = heapq.heappop(q)
        idx += 1
        
        

arr = [5, 2, 3, 1, 4, 7 , 12, 8, 10, 11]
k = 2
print(nearlySorted(arr, k))

# def nearlySorted(arr, k):
#     n = len(arr)
    
#     i = 0
    
#     while i < n:
#         j = 1
#         while j <= k and i + j < n:
#             if arr[i] > arr[i + j]:
#                 arr[i], arr[i + j] = arr[i + j], arr[i]
#             j += 1
#         i += 1        
#     return arr
            
            


# arr = [5, 2, 3, 1, 4, 7 , 12, 8, 10, 11]
# k = 10
# print(nearlySorted(arr, k))

