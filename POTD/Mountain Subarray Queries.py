# Check Each query Independently - O(n × q) Time and O(1) Space

# def processQueries(arr, queries):
    
#     n = len(arr)
#     m = len(queries)
#     res = [False for _ in range(m)]
    
#     for i in range(m):
#         start = queries[i][0]
#         end = queries[i][1]
#         print(queries[i])
        
#         while start <= end - 1 and arr[start] <= arr[start + 1]:
#             start += 1
#             print("ascending", start)
        

#         while start <=end - 1 and arr[start] >= arr[start + 1]:
#             start += 1
#             print("descending", start)
                
        
#         print("end", start)   
#         if start == end:
#             res[i] = True
            
#     return res


def processQueries(arr, queries):
    n = len(arr)
    res = []
     
    dec_idx = [i for i in range(n)]
    inc_idx = [i for i in range(n)]
     
    for i in range(n - 2, -1, -1):
        if arr[i] <= arr[i + 1]:
            dec_idx[i] = dec_idx[i + 1]
    
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            inc_idx[i] = inc_idx[i - 1]
            
    for s, e in queries:
        res.append(dec_idx[s] >= inc_idx[e])
        
    return res


arr = [9, 8, 7, 6, 7, 7, 7, 7 , 8, 9, 8, 7, 6, 5, 4]
queries = [[0, 3], [0, 7], [3, 9], [0, 4], [9, 14]]

print(processQueries(arr, queries))

    
