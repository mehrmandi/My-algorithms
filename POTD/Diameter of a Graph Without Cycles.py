# Given an undirected graph(with no cycles) represented using an adjacency list adj[][], find the diameter of the graph.
# The diameter of a graph(sometimes called the width) is the number of edges on the longest path between two nodes in the graph.

# Note: Graph do not contain any disconnected component.

# Finding ends of diameter - O(n) Time and O(n) Space

def dfsPrune(curr, adj, visited):
    if visited[curr]:
        return
    visited[curr] = True
    for next in adj[curr]:
        # remove back edge to make it a rooted tree
        adj[next].remove(curr)
        dfsPrune(next, adj, visited)


def findHeight(curr, adj, height):
    if height[curr] != -1:
        return height[curr]

    # leaf node has height = 0
    temp = 0
    for next_node in adj[curr]:
        temp = max(temp, 1 + findHeight(next_node, adj, height))

    height[curr] = temp
    return height[curr]


def diameter(adj):
    n = len(adj)
    visited = [False] * n
    height = [-1] * n

    # root the tree at 0
    dfsPrune(0, adj, visited)

    visited = [False] * n
    findHeight(0, adj, height)

    res = 0
    for i in range(n):
        firstMax = -1
        secondMax = -1

        for next in adj[i]:
            hVal = height[next]
            if hVal > firstMax:
                secondMax = firstMax
                firstMax = hVal
            elif hVal > secondMax:
                secondMax = hVal

        # take 2 children with max distance from root = i
        if firstMax != -1 and secondMax != -1:
            res = max(res, 2 + firstMax + secondMax)
        elif firstMax != -1:
            res = max(res, 1 + firstMax)

    return res


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


if __name__ == "__main__":
    V = 5
    adj = []

    # creating adjacency list
    for i in range(V):
        adj.append([])

    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)

    res = diameter(adj)
    print(res)
