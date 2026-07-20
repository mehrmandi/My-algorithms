class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def postOrder(root):
    res = []
    def postOrderRec(root):
        if not root:
            return
        
        postOrderRec(root.left)
        postOrderRec(root.right)
        res.append(root.data)

    postOrderRec(root)
    return res


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

print(postOrder(root))


#  Create binary tree
#       20
#       /  \
#     8     22
#    / \    / \
#   5   3  4   25
#  / \  / \    /
# 2   1 10 14  28


