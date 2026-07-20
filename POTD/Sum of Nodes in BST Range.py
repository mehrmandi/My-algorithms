# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None


# def inOrderTraversal(root, l, r, res):
#     if not root:
#         return
    
#     inOrderTraversal(root.left, l, r, res)
#     if l <= root.data <= r:
#         res[0] += root.data
        
#     inOrderTraversal(root.right, l, r, res)
    
    
# def nodeSum(root, l, r):
#     res = [0]
    
#     inOrderTraversal(root, l, r, res)
    
#     return res[0]


# root = Node(8)
# root.left = Node(5)
# root.right = Node(11)
# root.left.left = Node(3)
# root.left.right = Node(6)
# root.right.right = Node(20)

# l , r = 11, 15

# print(nodeSum(root, l, r))


# Node strcuture
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def nodeSum(root, l, r):
    if root is None:
        return 0

    #  If root value is less than range.
    #  all nodes in its left subtree
    #  will be less than range
    if root.data < l:
        return nodeSum(root.right, l, r)

    #  If root value is greater than range.
    #  all nodes in its right subtree
    #  will be greater than range
    elif root.data > r:
        return nodeSum(root.left, l, r)

    # If root value lies in the range.
    left = nodeSum(root.left, l, r)
    right = nodeSum(root.right, l, r)

    return left + right + root.data


if __name__ == "__main__":

    # BST
    #       22
    #      /  \
    #    12    30
    #   /  \
    #  8    20
    root = Node(8)
    root.left = Node(5)
    root.right = Node(11)
    root.left.left = Node(3)
    root.left.right = Node(6)
    root.right.right = Node(20)
    l = 11
    r = 15

    print(nodeSum(root, l, r))



