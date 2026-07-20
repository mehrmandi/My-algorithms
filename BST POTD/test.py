class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


# Recursive function to find the parent
# of the target node
def find_parent(root, target, parent):
    if root is None:
        return -1

    # If current node is the target,
    # return its parent
    if root.data == target:
        return parent
    print("root", root.data)
    # Recursively search in left subtree
    left_search = find_parent(root.left,
                              target, root.data)

    if left_search != -1:
        return left_search

    # Recursively search in right subtree
    return find_parent(root.right, target, root.data)


if __name__ == "__main__":
    # Representation of the given tree
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    target = 3
    parent = find_parent(root, target, -1)

    print(parent)