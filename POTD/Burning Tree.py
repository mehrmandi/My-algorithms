from collections import deque


# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None
        
        
# def nodeConnection(parent, node, connect):
#     if not node: 
#         return connect
    
#     connect[node.data] = [parent.data]
    
#     if node.left:
#         connect[node.data].append(node.left.data)
#         nodeConnection(node, node.left, connect)
        
#     if node.right:
#         connect[node.data].append(node.right.data)
#         nodeConnection(node, node.right, connect)
        
#     return connect

# def burningTree(root, target):
#     if not root:
#         return 0
#     connections = {root.data:[]}
#     q = deque([[target]])
#     visited = [target]
#     time = 0
#     if root.left:
#         connections[root.data].append(root.left.data)
#         nodeConnection(root, root.left, connections)
    
#     if root.right:
#         connections[root.data].append(root.right.data)
#         nodeConnection(root, root.right, connections)
            
#     while q:
#         sub = []
#         curr = q.popleft()
#         for i in range(len(curr)):
#             sub_curr = curr[i]
#             for j in range(len(connections[sub_curr])):
#                 if connections[sub_curr][j] not in visited:
#                     sub.append(connections[sub_curr][j])
#                     visited.append(connections[sub_curr][j])
#         if sub:
#             q.append(sub)
#             time += 1
            
#     return time
    

    
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# # root.right.left = Node(5)
# root.right.right = Node(7)
# root.left.left.left = Node(8)
# root.left.right.right = Node(10)

# target = 3


# print(burningTree(root, target))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def map_parents(root, parent_map):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            parent_map[node.left] = node
            queue.append(node.left)
        if node.right:
            parent_map[node.right] = node
            queue.append(node.right)


def min_time_to_burn_tree(root, target):
    if not root:
        return 0

    parent_map = {}
    map_parents(root, parent_map)

    # Locate the target node
    queue = deque()

    def find_target(node):
        if not node:
            return None
        if node.val == target:
            queue.append(node)
            return
        find_target(node.left)
        find_target(node.right)

    find_target(root)
    print(queue)

    visited = set(queue)
    time = 0

    # Start BFS to spread fire
    while queue:
        size = len(queue)
        found_new = False
        for _ in range(size):
            node = queue.popleft()

            for neighbor in [node.left, node.right, parent_map.get(node)]:
                if neighbor and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    found_new = True

        if found_new:
            time += 1

    return time


# Example Usage
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), TreeNode(7)))
target = 2
print(min_time_to_burn_tree(root, target))  # Output: 3


# Python Program to find the minimum time
# required to burn the complete binary tree
# [Expected Approach] Using Queue - O(n) Time and O(n) Space--------------------

# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None


# def minTime(root, target):

#     # Base case
#     if root is None:
#         return -1

#     q = deque([root])
#     tar = None

#     # Dictionary to map child nodes to
#     # parent nodes
#     par = {root: None}

#     while q:
#         curr = q.popleft()

#         # Set tar = curr if value is equal
#         if curr.data == target:
#             tar = curr

#         # Map the left child to its parent
#         if curr.left:
#             par[curr.left] = curr
#             q.append(curr.left)

#         # Map the right child to its parent
#         if curr.right:
#             par[curr.right] = curr
#             q.append(curr.right)

#     # Dictionary to check if a node has
#     # been visited or not
#     vis = {}

#     ans = -1

#     q.append(tar)

#     while q:
#         size = len(q)
#         for _ in range(size):
#             curr = q.popleft()
#             vis[curr] = True

#             # Push the left child node
#             if curr.left and not vis.get(curr.left, False):
#                 q.append(curr.left)

#             # Push the right child node
#             if curr.right and not vis.get(curr.right, False):
#                 q.append(curr.right)

#             # Push the parent node
#             if par[curr] and not vis.get(par[curr], False):
#                 q.append(par[curr])

#         # Increment the answer
#         ans += 1

#     return ans


# if __name__ == '__main__':

#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)

#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.left = Node(6)
#     root.right.right = Node(7)

#     target = 2

#     print(minTime(root, target))


# [Alternate Approach] Using Recursion - O(n) Time and O(h) Space-----------------------------


# Python Program to find the minimum time
# required to burn the complete binary tree
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# # Function to find the depth
# # from the root.


# def findDepth(root):
#     if root is None:
#         return 0

#     left = findDepth(root.left)
#     right = findDepth(root.right)

#     return max(left, right) + 1

# # This function returns the distance of current
# # node from the target node. Returns -1 if
# # target node is not found.


# def findTarNode(root, target, ans):

#     # base case
#     if root is None:
#         return -1

#     # if current node is the target, find the
#     # depth of root, compare it with ans and
#     # return 1.
#     if root.data == target:
#         depth = findDepth(root) - 1
#         ans[0] = max(ans[0], depth)
#         return 1

#     left = findTarNode(root.left, target, ans)

#     # If target node is found in the left subtree
#     # ,then compare the depth of right subtree and dis
#     # of target node with ans.
#     if left != -1:
#         depth = findDepth(root.right)
#         ans[0] = max(ans[0], left + depth)
#         return left + 1

#     # If target node is found in the right subtree
#     # ,then compare the depth of left subtree and dis
#     # of target node with ans.
#     right = findTarNode(root.right, target, ans)
#     if right != -1:
#         depth = findDepth(root.left)
#         ans[0] = max(ans[0], right + depth)
#         return right + 1

#     # if target node is not found,
#     # return -1.
#     return -1


# def minTime(root, target):
#     ans = [0]
#     findTarNode(root, target, ans)
#     return ans[0]


# if __name__ == "__main__":

#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)

#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.left = Node(6)
#     root.right.right = Node(7)

#     target = 2

#     print(minTime(root, target))
