# Python program to find maximum path
# sum between two leaves of a binary tree

# Python program to find the diameter
# of a binary tree.

# # [Expected Approach] Using Bottom Up Recursive - O(n) Time and O(h) Space--------------------------------------------


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Recursive function to find the height of root and 
# also calculate the diameter of the tree.
def diameterRecur(root, res):

    # Base case: tree is empty
    if root is None:
        return 0

    # find the height of left and right subtree
    # (it will also find of diameter for left 
    # and right subtree).
    lHeight = diameterRecur(root.left, res)
    rHeight = diameterRecur(root.right, res)

    # Check if diameter of root is greater
    # than res.
    res[0] = max(res[0], lHeight + rHeight)

    # return the height of current subtree.
    return 1 + max(lHeight, rHeight)

# Function to get diameter of a binary tree
def diameter(root):
    res = [0]
    diameterRecur(root, res)
    return res[0]

if __name__ == "__main__":

    # Constructed binary tree is
    #          5
    #        /   \
    #       8     6
    #      / \   /
    #     3   7 9
    root = Node(5)
    root.left = Node(8)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(9)

    print(diameter(root))


# Example usage:


root = Node(13)
root.left = Node(8)
# root.right = Node(3)
# root.left.left = Node(4)
root.left.right = Node(22)
root.left.right.left = Node(66)
root.left.right.right = Node(27)

print(diameter_of_binary_tree(root))

# 13 8 N N 22 66 27 N N N N


# [Expected Approach] Using Bottom Up Recursive - O(n) Time and O(h) Space--------------------------------------------

# Python program to find the diameter
# of a binary tree.

# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None

# # Recursive function to find the height of root and
# # also calculate the diameter of the tree.


# def diameterRecur(root, res):

#     # Base case: tree is empty
#     if root is None:
#         return 0

#     # find the height of left and right subtree
#     # (it will also find of diameter for left
#     # and right subtree).
#     lHeight = diameterRecur(root.left, res)
#     rHeight = diameterRecur(root.right, res)

#     # Check if diameter of root is greater
#     # than res.
#     res[0] = max(res[0], lHeight + rHeight)

#     # return the height of current subtree.
#     return 1 + max(lHeight, rHeight)

# # Function to get diameter of a binary tree


# def diameter(root):
#     res = [0]
#     diameterRecur(root, res)
#     return res[0]


# if __name__ == "__main__":

#     # Constructed binary tree is
#     #          5
#     #        /   \
#     #       8     6
#     #      / \   /
#     #     3   7 9
#     root = Node(5)
#     root.left = Node(8)
#     root.right = Node(6)
#     root.left.left = Node(3)
#     root.left.right = Node(7)
#     root.right.left = Node(9)

#     print(diameter(root))
