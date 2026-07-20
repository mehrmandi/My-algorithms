# Time Complexity: O(n)
# Auxiliary Space: O(n), due to recursion stack


# from collections import deque


# def reverseQueue(q):
#     if not q:
#         return

#     # remove front element
#     front = q.popleft()

#     # reverse remaining queue
#     reverseQueue(q)

#     # insert removed element at the rear
#     q.append(front)


# if __name__ == '__main__':
#     q = deque([5, 10, 15, 20, 25])
#     reverseQueue(q)
#     while q:
#         print(q.popleft(), end=' ')




def reverseQueue(q):
    n = len(q)
    left, right = 0, n - 1
    
    while left <= right:
        q[left], q[right] = q[right], q[left]
        left += 1
        right -= 1
        
    return q
    

q = [5, 10, 15, 20, 25]
print(reverseQueue(q))
