class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v


# Inorder Traversal
def InorderTraversal(root, res, t):
    if not root:
        return False

    if (t - root.data) in res:
        return True

    res.add(root.data)

    return InorderTraversal(root.left, res, t) or InorderTraversal(root.right, res, t)


def pairSum(root, target):
    res = set()
    return InorderTraversal(root, res, target)




# root = [9, 5, 10, 2, 6, N, 12], target = 23
target = 23
root = Node(9)
root.left = Node(5)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(6)
# root.right.left = Node(150)
root.right.right = Node(12)

# print(InorderTraversal(root, [], target, f = False))
print(pairSum(root, target))