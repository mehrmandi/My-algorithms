class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def is_dead_end_util(root, min_val, max_val):
    # Base case: if the current node is None, there's no dead end here.
    if root is None:
        return False

    # If the allowable range has narrowed to a single value,
    # no further insertion is possible, hence a dead end
    if min_val == max_val:
        return True

    # Check the left and right subtrees with updated ranges.
    return (is_dead_end_util(root.left, min_val, root.data - 1) or
            is_dead_end_util(root.right, root.data + 1, max_val))


def is_dead_end(root):
    # Start with the range [1, infinity]
    return is_dead_end_util(root, 1, float('inf'))

# Testing the implementation with the provided example:
# Constructing the BST:
#          8
#         / \
#        5   9
#       / \
#      2   7
#     /
#    1


root = Node(8)
root.left = Node(5)
root.right = Node(9)
root.left.left = Node(2)
root.left.right = Node(7)
root.left.left.left = Node(1)

# Checking for a dead end:
print(is_dead_end(root))  # Expected output: True
        
    