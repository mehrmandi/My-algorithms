class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v


def inOrderTraversal(root, res):
    if not root:
        return
    inOrderTraversal(root.left, res)
    res.append(root.data)
    inOrderTraversal(root.right, res)


def TraversePrint(root):
    res = []
    inOrderTraversal(root, res)
    return res


# [1, 7, 10, 8, 10, 5, 6, 6]
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.left.left.right = Node(1)
root.left.left.left = Node(2)
root.right.left = Node(4)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right.right = Node(25)
root.right.right.left = Node(28)

print(TraversePrint(root))
# print(inOrderTraversal(root, []))