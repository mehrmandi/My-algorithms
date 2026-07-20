# [Approach 1] Using BFS traversal - O(V+E) Time and O(V) Space

from collections import deque


# Definition for a Node
class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []


# Clone the graph
def cloneGraph(node):
    if not node:
        return None

    # Map to hold original nodes as keys and their clones as values
    mp = {}

    # Initialize BFS queue
    q = deque([node])

    # Clone the starting node
    mp[node] = Node(node.val)

    while q:
        current = q.popleft()

        for neighbor in current.neighbors:

            # If neighbor not cloned yet
            if neighbor not in mp:
                mp[neighbor] = Node(neighbor.val)
                q.append(neighbor)

            # Link clone of neighbor to the clone of the current node
            mp[current].neighbors.append(mp[neighbor])

    return mp[node]


# Build graph
def buildGraph():
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)

    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2, node4]
    node4.neighbors = [node3]

    return node1


# Compare two graphs structurally and by values
def compareGraphs(n1, n2, visited):
    if not n1 or not n2:
        return n1 == n2

    if n1.val != n2.val or n1 is n2:
        return False

    visited[n1] = n2

    if len(n1.neighbors) != len(n2.neighbors):
        return False

    for i in range(len(n1.neighbors)):
        neighbor1 = n1.neighbors[i]
        neighbor2 = n2.neighbors[i]

        if neighbor1 in visited:
            if visited[neighbor1] != neighbor2:
                return False

        else:
            if not compareGraphs(neighbor1, neighbor2, visited):
                return False

    return True


# Driver
if __name__ == "__main__":
    original = buildGraph()
    cloned = cloneGraph(original)
    result = compareGraphs(original, cloned, {})
    print("true" if result else "false")


# [Approach 2] Using DFS traversal - O(V+E) Time and O(V) Space---------------------
# Definition for a Node
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
#
# # Map to hold original node to its copy
# copies = {}
#
# # Function to clone the graph
# def cloneGraph(node):
#     # If the node is None, return None
#     if not node:
#         return None
#
#     # If node is not yet cloned, clone it
#     if node not in copies:
#         # Create a clone of the node
#         clone = Node(node.val)
#         copies[node] = clone
#
#         # Recursively clone neighbors
#         for neighbor in node.neighbors:
#             clone.neighbors.append(cloneGraph(neighbor))
#
#     # Return the clone
#     return copies[node]
#
#
# def buildGraph():
#     node1 = Node(0)
#     node2 = Node(1)
#     node3 = Node(2)
#     node4 = Node(3)
#     node1.neighbors = [node2, node3]
#     node2.neighbors = [node1, node3]
#     node3.neighbors = [node1, node2, node4]
#     node4.neighbors = [node3]
#
#     return node1
#
# # Compare two graphs for structural and value equality
# def compareGraphs(node1, node2, visited):
#     if not node1 or not node2:
#         return node1 == node2
#
#     if node1.val != node2.val or node1 is node2:
#         return False
#
#     visited[node1] = node2
#
#     if len(node1.neighbors) != len(node2.neighbors):
#         return False
#
#     for i in range(len(node1.neighbors)):
#         n1 = node1.neighbors[i]
#         n2 = node2.neighbors[i]
#
#         if n1 in visited:
#             if visited[n1] != n2:
#                 return False
#         else:
#             if not compareGraphs(n1, n2, visited):
#                 return False
#
#     return True
#
# # Driver Code
# if __name__ == "__main__":
#     original = buildGraph()
#
#     # Clone the graph using DFS
#     cloned = cloneGraph(original)
#
#     # Compare original and cloned graph
#     visited = {}
#     print("true" if compareGraphs(original, cloned, visited) else "false")