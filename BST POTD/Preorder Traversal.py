class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def preOrder(root):
    res = []

    def preOrderRec(root):
        if not root:
            return

        res.append(root.data)
        preOrderRec(root.left)
        preOrderRec(root.right)
        

    preOrderRec(root)
    return res


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right.right = Node(25)
root.right.right.left = Node(28)
root.left.left.right = Node(1)
root.left.left.left = Node(2)

print(preOrder(root))
