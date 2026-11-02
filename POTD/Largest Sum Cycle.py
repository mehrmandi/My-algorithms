# Given an array edge[] of size n, there are n cells numbered from 0 to n - 1. Each cell has at most one outgoing edge.

# For every cell i:

# edge[i] is the cell reached from i in one step.
# edge[i] = -1 means that cell i has no outgoing edge.
# A cycle is a sequence of cells where, by following the outgoing edges, we eventually return to the starting cell. The sum of a cycle is the sum of the indices of all cells in that cycle.

# Return the maximum cycle sum. If there is no cycle, return -1.

# Kahn's Algorithm - O(n) Time and O(n) Space

from collections import deque


def largestSumCycle(edge):
    n = len(edge)

    indegree = [0] * n

    # Calculate the indegree of every cell
    for i in range(n):
        if edge[i] != -1:
            indegree[edge[i]] += 1

    q = deque()

    # Add all cells with indegree 0 to the queue
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    # Remove all cells that cannot be part of a cycle
    while q:
        node = q.popleft()

        next_node = edge[node]

        if next_node != -1:
            indegree[next_node] -= 1

            # If indegree becomes 0, it cannot be part of a cycle
            if indegree[next_node] == 0:
                q.append(next_node)

    ans = -1
    visited = [0] * n

    # Traverse the remaining cells to find all cycles
    for i in range(n):
        if indegree[i] > 0 and visited[i] == 0:
            total = 0
            node = i

            # Calculate the sum of the current cycle
            while visited[node] == 0:
                visited[node] = 1
                total += node
                node = edge[node]

            ans = max(ans, total)

    return ans


# Driver Code
if __name__ == "__main__":
    edge = [1, 2, 0, -1]


#  DFS With 3 States - O(n) Time and O(n) Space    
    
# def dfs(node, edge, state, parent):

#     # Mark the current cell as being visited
#     state[node] = 1

#     next_node = edge[node]

#     # No outgoing edge
#     if next_node == -1:
#         state[node] = 2
#         return -1

#     # Visit the next cell if it is unvisited
#     if state[next_node] == 0:
#         parent[next_node] = node

#         sum_val = dfs(next_node, edge, state, parent)

#         # Mark the current cell as completely processed
#         state[node] = 2

#         return sum_val

#     # A cycle is found if the next cell is in the current path
#     if state[next_node] == 1:
#         sum_val = next_node
#         cur = node

#         # Calculate the sum of the cycle
#         while cur != next_node:
#             sum_val += cur
#             cur = parent[cur]

#         # Mark the current cell as completely processed
#         state[node] = 2

#         return sum_val

#     # The next cell is already completely processed
#     state[node] = 2

#     return -1


# def largestSumCycle(edge):
#     n = len(edge)
#     ans = -1

#     state = [0] * n
#     parent = [-1] * n

#     # Try starting DFS from every unvisited cell
#     for i in range(n):
#         if state[i] == 0:
#             ans = max(ans, dfs(i, edge, state, parent))

#     return ans


# # Driver Code
# if __name__ == "__main__":
#     edge = [1, 2, 0, -1]

#     print(largestSumCycle(edge))


