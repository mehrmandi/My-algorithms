# from collections import deque
from collections import deque
from collections import defaultdict


# def countPaths(edges, V,  src, dest):
#     adj = [[] for _ in range(V)]
#     paths = [0 for _ in range(V + 1)]

#     for edge in edges:
#         adj[edge[0]].append(edge[1])
        
#     q = deque([src])

#     while q:
#         node = q.popleft()

#         paths[node] += 1

#         for i in adj[node]:
#             q.append(i)

#     return paths[dest]


# edges = [[0, 1], [1, 2], [1, 3], [2, 3]]
# V = 4
# src = 0
# dest = 3
# print(countPaths(edges, V, src, dest))
# # {0: [1, 3], 2: [0, 1], 1: [3]}


def count_paths(edges, V, src, dest):

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    memo = {}

    def dfs(node):
        if node == dest:
            return 1
        if node in memo:
            return memo[node]

        total_paths = 0
        for nei in graph[node]:
            total_paths += dfs(nei)

        memo[node] = total_paths
        return total_paths

    return dfs(src)


edges = [[0, 1], [1, 2], [1, 3], [2, 3]]
V = 4
src = 0
dest = 3
print(count_paths(edges, V, src, dest))


# Python program to find Number of paths from source
# to destination in a directed acyclic graph
# [Expected Approach - 2] Using DFS + Topological Sort - O(V + E) time and O(V) space-----------------------------------

# def countPaths(edges, V, src, dest):
#     adj = [[] for _ in range(V)]
#     inDeg = [0] * V

#     # Create adjancecny list and
#     # find in-degree
#     for e in edges:
#         adj[e[0]].append(e[1])
#         inDeg[e[1]] += 1

#     q = deque()
#     for i in range(V):
#         if inDeg[i] == 0:
#             q.append(i)

#     paths = [0] * V
#     paths[src] = 1

#     while q:
#         u = q.popleft()

#         # For each edge u->v, if number of
#         # paths starting from source node to
#         # u'th node is x, then the same paths
#         # will be present for v'th node.
#         for v in adj[u]:
#             paths[v] += paths[u]
#             inDeg[v] -= 1
#             if inDeg[v] == 0:
#                 q.append(v)

#     return paths[dest]


# if __name__ == "__main__":
#     V = 4
#     src = 2
#     dest = 3
#     edges = [[0, 1], [0, 3], [2, 0], [2, 1], [1, 3]]
#     print(countPaths(edges, V, src, dest))


# Python program to find Number of paths from source
# to destination in a directed acyclic graph
# [Expected Approach - 1] Using DFS + DP - O(V + E) time and O(V) space--------------------------------------
# def dfs(u, dest, adj, memo):

#     # If destination is reached
#     if u == dest:
#         return 1

#     # If number of paths from this node
#     # is memoized
#     if memo[u] != -1:
#         return memo[u]

#     count = 0
#     for v in adj[u]:
#         count += dfs(v, dest, adj, memo)

#     memo[u] = count
#     return count


# def countPaths(edges, V, src, dest):
#     adj = [[] for _ in range(V)]
#     for e in edges:
#         adj[e[0]].append(e[1])
#     memo = [-1] * V
#     return dfs(src, dest, adj, memo)


# if __name__ == "__main__":
#     V = 4
#     src = 2
#     dest = 3
#     edges = [[0, 1], [0, 3], [2, 0], [2, 1], [1, 3]]
#     print(countPaths(edges, V, src, dest))
