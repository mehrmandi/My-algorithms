class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# def BSTCheck(node, min_val, max_val):
#     if node is None:
#         return True
#
#     if node.data < min_val or node.data > max_val:
#         return False
#
#     return (BSTCheck(node.left, min_val, node.data - 1) and
#             BSTCheck(node.right, node.data + 1, max_val))
#
# def isBST(root):
#     return BSTCheck(root, float('-inf'), float('inf'))


def inorder(root, prev):
    if root is None:
        return True

    # Recursively check the left subtree
    if not inorder(root.left, prev):
        return False

    # Check the current node value against the previous value
    if prev[0] >= root.data:
        return False

    # Update the previous value to the current node's value
    prev[0] = root.data

    # Recursively check the right subtree
    return inorder(root.right, prev)

# Function to check if the tree is a valid BST
def isBST(root):
    prev = [float('-inf')]
    return inorder(root, prev)


# root = [2, 1, 3, N, N, N, 5]

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.right = Node(25)
root.right.left = Node(9)


print(isBST(root))
