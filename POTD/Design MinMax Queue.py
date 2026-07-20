from collections import deque

class SpecialQueue:
    def __init__(self):
        # Define Data Structures
        self.q1 = deque()
        self.q2 = deque()
        self.q3 = deque()

    def enqueue(self, x):
        # Insert element into the queue
        self.q1.append(x)
        while self.q2 and self.q2[-1] > x:
            self.q2.pop()
        self.q2.append(x)
        while self.q3 and self.q3[-1] < x:
            self.q3.pop()
        self.q3.append(x)

    def dequeue(self):
        if not self.q1:
            return False
        # Remove element from the queue
        first_val = self.q1.popleft()
        if self.q2[0] == first_val:
            self.q2.popleft()
        
        if self.q3[0] == first_val:
            self.q3.popleft()
            
        

    def getFront(self):
        # Get front element
        if not self.q1:
            return False
        return self.q1[0]
        

    def getMin(self):
        # Get minimum element
        if not self.q2:
            return False
        
        return self.q2[0]
        

    def getMax(self):
        # Get maximum element
        if not self.q3:
            return False
        
        return self.q3[0]
        



q = 6
queries = [[1, 4], [1, 2], [3], [4], [2], [5]]

# 7
1 4
2
1 6
1 12
5
1 4
4
