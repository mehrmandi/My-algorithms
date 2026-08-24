# Given the root of a binary tree, check whether it is a Binary Search Tree(BST) or not . A binary tree is considered a BST if it satisfies the following properties:

# All nodes in the left subtree of a node have values less than the node's value.
# All nodes in the right subtree of a node have values greater than the node's value.
# Both the left and right subtrees are also Binary Search Trees.
# Return true if the given binary tree is a BST
# otherwise, return false.

# Using Inorder Traversal - O(n) Time and O(h) Space

# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None


# def inorder(root, prev):
#     if root is None:
#         return True

#     # Recursively check the left subtree
#     if not inorder(root.left, prev):
#         return False

#     # Check the current node value against the previous value
#     if prev[0] >= root.data:
#         return False

#     # Update the previous value to the current node's value
#     prev[0] = root.data

#     # Recursively check the right subtree
#     return inorder(root.right, prev)

# # Function to check if the tree is a valid BST
# def isBST(root):
#     prev = [float('-inf')]
#     return inorder(root, prev)


#------------------------------------------------------------------------------
# Using Morris Traversal - O(n) Time and O(1) Space

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

#  Function to check if the binary tree
#  is a BST using Morris Traversal


def isBST(root):
    curr = root
    prevValue = float('-inf')

    while curr:
        if curr.left is None:
            if curr.data <= prevValue:

                # Not in ascending order
                return False
            prevValue = curr.data
            curr = curr.right
        else:

            # Find the inorder predecessor of curr
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right

            if pre.right is None:

                # Create a temporary
                # thread to the curr node
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None

                if curr.data <= prevValue:

                    # Not in ascending order
                    return False
                prevValue = curr.data
                curr = curr.right

    return True

# root = [2, 1, 3, N, N, N, 5]

root = Node(2)
root.right = Node(4)
root.right.left = Node(1)


print(isBST(root))
