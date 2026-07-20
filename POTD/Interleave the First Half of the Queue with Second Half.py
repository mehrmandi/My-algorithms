# def rearrangeQueue(q):
#     n = len(q)
#     mid = n // 2
#     idx = [[q[i], i] for i in range(n)]
    
#     for i in range(1, mid):
#         idx[i][1] = i + i
#         idx[mid + i - 1][1] = 2 * i - 1
        
#     for i in range(1, n - 1):
#         q[idx[i][1]] = idx[i][0]
    
    
#     return q
# [Expected Approach 2] Using Queue - O(n) Time and O(n) Space--------------------

from collections import deque
def rearrangeQueue(q):
    n = len(q)

    # copy elements to temporary array
    arr = list(q)
    q.clear()

    # Interleave elements back into the queue
    for i in range(n // 2):
        q.append(arr[i])
        q.append(arr[i + n // 2])

    
q = [2, 4, 3, 1, 8, 9, 5, 6]
print(rearrangeQueue(q))
# 2 8 4 9 3 5 1 6
