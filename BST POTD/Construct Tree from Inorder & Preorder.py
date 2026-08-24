# Given inorder and preorder traversals of a Binary Tree in array inorder[] and preorder[] respectively, Construct the Binary Tree and return it’s root.

# Note: All values in inorder[] and preorder[] are distinct.

#  Using Pre-order traversal and Hash map - O(n) Time and O(n) Space

from collections import deque
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Recursive function to build the binary tree.


def buildTreeRecur(mp, preorder, preIndex, left, right):

    # For empty inorder array, return None
    if left > right:
        return None

    rootVal = preorder[preIndex[0]]
    preIndex[0] += 1

    root = Node(rootVal)

    index = mp[rootVal]

    # Recursively create the left and right subtree.
    root.left = buildTreeRecur(mp, preorder, preIndex, left, index - 1)
    root.right = buildTreeRecur(mp, preorder, preIndex, index + 1, right)

    return root

# Function to construct tree from its inorder and preorder traversals


def buildTree(inorder, preorder):

    # Hash map that stores index of a root element in inorder array
    mp = {value: idx for idx, value in enumerate(inorder)}
    preIndex = [0]

    return buildTreeRecur(mp, preorder, preIndex, 0, len(inorder) - 1)


def getHeight(root, h):
    if root is None:
        return h - 1
    return max(getHeight(root.left, h + 1), getHeight(root.right, h + 1))


def levelOrder(root):
    queue = deque([[root, 0]])
    lastLevel = 0

    # function to get the height of tree
    height = getHeight(root, 0)

    # printing the level order of tree
    while queue:
        node, lvl = queue.popleft()

        if lvl > lastLevel:
            print()
            lastLevel = lvl

        # all levels are printed
        if lvl > height:
            break

        # printing null node
        print("N" if node.data == -1 else node.data, end=" ")

        # null node has no children
        if node.data == -1:
            continue

        if node.left is None:
            queue.append([Node(-1), lvl + 1])
        else:
            queue.append([node.left, lvl + 1])

        if node.right is None:
            queue.append([Node(-1), lvl + 1])
        else:
            queue.append([node.right, lvl + 1])






inorder = [3, 1, 4, 0, 2, 5]
preorder = [0, 1, 3, 4, 2, 5]

print(buildTree(preorder, inorder))
