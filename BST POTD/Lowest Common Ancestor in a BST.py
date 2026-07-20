class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v


def lca(root, n1, n2):

    if not root:
        return None

    if root.data == n1 or root.data == n2:
        return root.data

    leftLca = lca(root.left, n1, n2)
    rightLca = lca(root.right, n1, n2)

    # print(leftLca, rightLca)

    if leftLca and rightLca:
        return root.data

    return leftLca if leftLca else rightLca

# def findPath(root, path, k):
#     # Baes Case
#     if root is None:
#         return False
#
#     # Store current node in path
#     path.append(root)
#
#     # If node value is equal to k, or
#     # if node exist in left subtree or
#     # if node exist in right subtree return true
#     if (root.data == k or
#         findPath(root.left, path, k)
#         or findPath(root.right, path, k)):
#         return True
#
#     # else remove root from path and return false
#     path.pop()
#     return False
#
# # Function to find lca of two nodes
# def lca(root, n1, n2):
#
#     # To store paths to n1 and n2 fromthe root
#     path1 = []
#     path2 = []
#
#     # Find paths from root to n1 and root to n2.
#     # If either n1 or n2 is not present , return -1
#     if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
#         return None
#
#     # Compare the paths to get the first different value
#     i = 0
#     while(i < len(path1) and i < len(path2)):
#         if path1[i] != path2[i]:
#             break
#         i += 1
#     return path1[i-1]


# 5 4 6 3 N N 7 N N N 8
target1 = 7
target2 = 8
root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(3)
# root.left.right = Node(12)
# root.left.right.left = Node(10)
# root.left.right.right = Node(14)
root.right.right = Node(7)
root.right.right.right = Node(8)



print(lca(root, target1, target2))
