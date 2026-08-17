# Given an integer n such that there is n × n Snakes and Ladders board with cells numbered from 1 to n*n, find the minimum number of dice throws required to reach cell n*n starting from cell 1. Given two arrays of even lengths:

# lad[], where each pair(lad[2*i], lad[2*i + 1]) represents the start and end of a ladder.
# sn[], where each pair(sn[2*i], sn[2*i + 1]) represents the start and end of a snake.
# If you land on the start cell of a snake or ladder, you must immediately move to its corresponding end cell.

# You have complete control over the outcome of each dice throw i.e., in a single move,  you can move forward by any number of cells from 1 to 6.

# If it is impossible to reach cell n*n, return -1.


# Using Breadth First Search (BFS) - O(n^2) Time and O(n^2) Space


from collections import deque

def minThrows(n, lad, sn):
    all_cell = n ** 2
    jump = list(range(all_cell + 1))

    # Ladders
    for i in range(0, len(lad), 2):
        jump[lad[i]] = lad[i + 1]

    # Snakes
    for i in range(0, len(sn), 2):
        jump[sn[i]] = sn[i + 1]
        
    visited = [False] * (all_cell + 1)
    
    q = deque([(1, 0)])
    visited[1] = True
    
    while q:
        cell, throw = q.popleft()
        if cell == all_cell:
            return throw
        
        # Try all possible dice outcomes.
        for dice in range(1, 7):
            new_cell = cell + dice
            
            if new_cell > all_cell:
                continue
            
            new_cell = jump[new_cell]
            
            if not visited[new_cell]:
               q.append((new_cell, throw + 1))
               visited[new_cell] = True 
            
    return -1
            

n = 6
lad = [3, 22, 5, 8, 11, 35, 20, 32]
sn = [17, 4, 19, 7, 34, 1, 21, 9]
print(minThrows(n, lad, sn))
