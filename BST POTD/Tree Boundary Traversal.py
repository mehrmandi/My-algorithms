class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def isLeaf(node):
    return node.left is None and node.right is None

def collectBoundaryLeft(root, res):
    if root is None or isLeaf(root):
        return
    res.append(root.data)
    if root.left:
        collectBoundaryLeft(root.left, res)
    elif not root.left and root.right:
        collectBoundaryLeft(root.right, res)

def collectLeaves(root, res):
    if root is None:
        return

    if isLeaf(root):
        res.append(root.data)
        return

    collectLeaves(root.left, res)
    collectLeaves(root.right, res)

def collectBoundrayRight(root, res):
    if root is None or isLeaf(root):
        return

    if root.right:
        collectBoundrayRight(root.right, res)
    elif not root.right and root.left:
        collectBoundrayRight(root.left, res)

    res.append(root.data)


# def insertLevelOrder(arr, i, n):
#     root = None
#     # Base case for recursion
#     if i < n:
#         root = Node(arr[i])
#
#         # insert left child
#         root.left = insertLevelOrder(arr, 2 * i + 1, n)
#
#         # insert right child
#         root.right = insertLevelOrder(arr, 2 * i + 2, n)
#
#     return root


def boundaryTraversal(root):
    rootarr = [root.data]
    left = []
    right = []
    leaves = []
    if not root.left and not root.right:
        return [root.data]

    collectBoundaryLeft(root.left, left)
    collectLeaves(root, leaves)
    collectBoundrayRight(root.right, right)
    print(left, leaves, right)
    return rootarr + left + leaves + right


# arr = 1 2 3 N N 4 N 5 N N N
root = Node(1)
# root.left = Node(2)
# # root.right = Node(3)
# # root.right.left = Node(6)
# root.left.right = Node(9)
# root.left.left = Node(4)
# root.left.left.left = Node(6)
# root.left.left.right = Node(5)
# root.left.right.right = Node(3)
# root.left.right.right.left = Node(7)
# root.left.right.right.right = Node(8)

print(boundaryTraversal(root))
