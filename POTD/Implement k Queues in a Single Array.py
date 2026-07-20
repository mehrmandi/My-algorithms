# from collections import deque


# class kQueues:

#     def __init__(self, n, k):
#         self.k = k
#         self.n = n
#         # Initialize your data members
#         self.queues = [deque() for _ in range(self.k)]
        
#     def enqueue(self, x, i):
#         # Enqueue element x into queue number i
#         self.queues[i].append(x)

#     def dequeue(self, i):
#         # Dequeue element from queue number i
#         if self.isEmpty(i):
#             return -1
#         else:
#             return self.queues[i].popleft()
        
#     def isEmpty(self, i):
#         if not self.queues[i]:
#             return True
#         else:
#             return False
#         # Check if queue i is empty

#     def isFull(self):
#         sum_len = 0
#         # Check if array is full
#         for i in range(self.k):
#             sum_len += len(self.queues[i])
            
#         if sum_len == self.n:
#             return True
#         else:
#             False


# [Expected Approach] Using Space Optimized Method - O(1) Time and O(n+k) Space--------------------
class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = [0] * n

        # Initialize all spaces as free
        self.freeIndex = 0
        for i in range(n - 1):
            self.next[i] = i + 1

        # -1 is used to indicate end of free list
        self.next[n - 1] = -1

    # Function to check if queue 'qn' is empty
    def isEmpty(self, qn):
        return self.front[qn] == -1

    # Function to check if array is full
    def isFull(self):
        return self.freeIndex == -1

    # Function to enqueue 'x' into queue 'qn'
    def enqueue(self, x, qn):
        # Check if array is full
        if self.isFull():
            return False

        # Get next free index
        i = self.freeIndex
        self.freeIndex = self.next[i]

        # If queue is empty, update
        # both front and rear
        if self.isEmpty(qn):
            self.front[qn] = i
        else:
            # Link new element to the previous rear
            self.next[self.rear[qn]] = i

        # Update rear
        self.rear[qn] = i

        # Store the element
        self.arr[i] = x

        # Mark end of queue
        self.next[i] = -1

        return True

    # Function to dequeue from queue 'qn'
    def dequeue(self, qn):
        # Check if queue is empty
        if self.isEmpty(qn):
            return -1

        # Get the front index of queue
        i = self.front[qn]

        # Update front
        self.front[qn] = self.next[i]

        # If queue becomes empty
        if self.front[qn] == -1:
            self.rear[qn] = -1

        # Add the dequeued position to free list
        self.next[i] = self.freeIndex
        self.freeIndex = i

        # Return the dequeued element
        return self.arr[i]


def result(n, k, queries):
    q = kQueues(n, k)
    res = []
    for arr in queries:
        if arr[0] == 1:
            q.enqueue(arr[1], arr[2])
        
        elif arr[0] == 2:
            res.append(q.dequeue(arr[1]))
            
        elif arr[0] == 3:
            res.append(q.isEmpty(arr[1]))
            
        else:
            res.append(q.isFull())
           
    return res

n = 4
k = 2
q = 8
queries = [[1, 5, 0], [1, 3, 0], [1, 1, 1], [
    2, 0], [1, 4, 1], [1, 1, 0], [3, 1], [4]]

print(result(n, k, queries))
