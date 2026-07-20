class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v
#
# def inorder(root, prev, first, second):
#     if not root:
#         return
#
#     inorder(root.left, prev, first, second)
#
#     if prev[0] and root.data < prev[0].data:
#         if not first:
#             first[0] = prev[0]
#         second[0] = root
#
#     prev[0] = root
#     inorder(root.data, prev, first, second)
#
# def recoverTree(root):
#     prev, first, second = [None], [None], [None]
#     if not root:
#         return
#
#     inorder(root, prev, first, second)
#     temp = first[0].data
#     first[0].data = second[0].data
#     second[0].data = temp


# ----------------------------------------------------------------------------

def findInorder(curr, inorder):
    if curr is None:
        return

    findInorder(curr.left, inorder)
    print(curr.data)
    inorder.append(curr.data)
    findInorder(curr.right, inorder)


def correctBSTUtil(root, inorder, index):
    if root is None:
        return

    correctBSTUtil(root.left, inorder, index)
    root.data = inorder[index[0]]
    index[0] += 1
    correctBSTUtil(root.right, inorder, index)


def correctBST(root):
    inorder = []
    findInorder(root, inorder)
    inorder.sort()
    index = [0]
    correctBSTUtil(root, inorder, index)
    print("******************")
    findInorder(root, inorder)




root = Node(6)
root.left = Node(10)
root.right = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(12)
root.right.left = Node(7)

#
# 1 2 3 6 7 10 12
findInorder(root, [])
print("----------------")
print(correctBST(root))


