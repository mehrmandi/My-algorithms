from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def leftViewBS(root):
    res = []
    visited = []
    if not root:
        return res

    queue = deque([(root, 0)])
    seen_level = set()

    while queue:
        node, level = queue.popleft()

        if level not in seen_level:
            res.append(node.data)
            seen_level.add(level)

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    return res


# root[] = [1, 2, 3, N, N, 4, N, N, 5, N, N]
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.left.right = Node(5)

print(leftViewBS(root))


# [Approach - 1] Using Depth-first search (DFS) - O(n) Time and O(n) Space


# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None


# def recLeftView(root, level, result):
#     if root is None:
#         return

#     if level == len(result):
#         result.append(root.data)

#     recLeftView(root.left, level + 1, result)
#     recLeftView(root.right, level + 1, result)


# def leftView(root):
#     result = []
#     recLeftView(root, 0, result)
#     return result


# # Main function
# if __name__ == "__main__":
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)

#     result = leftView(root)
#     print(' '.join(map(str, result)))  # Output: 1 2 4


# [Approach - 2] Using Level Order Traversal (BFS) - O(n) Time and O(n) Space

# Python program to print left view of Binary Tree
# using Level Order Traversal


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# Function to return the left view of the binary tree


# def LeftView(root):
#     result = []

#     if root is None:
#         return result

#     # Queue for level order traversal
#     q = deque([root])

#     while q:

#         # Number of nodes at the current level
#         level_size = len(q)

#         for i in range(level_size):
#             curr = q.popleft()

#             # If it's the first node of the
#             # current level
#             if i == 0:
#                 result.append(curr.data)

#             # Enqueue left child
#             if curr.left is not None:
#                 q.append(curr.left)

#             # Enqueue right child
#             if curr.right is not None:
#                 q.append(curr.right)

#     return result


# if __name__ == "__main__":

#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)

#     result = LeftView(root)
#     for val in result:
#         print(val, end=" ")
#     print()
