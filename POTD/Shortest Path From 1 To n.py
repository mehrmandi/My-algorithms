# Consider a directed graph whose vertices are numbered from 1 to n. There is an edge from a vertex i to a vertex j if and only if either j = i + 1 or j = 3 * i. The task is to find the minimum number of edges in a path from vertex 1 to vertex n.

# Reverse Greedy - O(log n) Time and O(1) Space

def minimumStep(n):
    res = 0
    
    while n > 1:
        if n % 3 == 0:
            res += 1
            n /= 3
        else:
            res += 1
            n -= 1
            
    return res


n = 4
print(minimumStep(n))