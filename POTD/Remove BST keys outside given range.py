from collections import deque

# Node structure


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Calculate Height


def getHeight(root, h):
    if root is None:
        return h - 1
    return max(getHeight(root.left, h + 1), getHeight(root.right, h + 1))

# Print Level order


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


def removekeys(root, l, r):

    if root is None:
        return None

    left = removekeys(root.left, l, r)

    right = removekeys(root.right, l, r)

    # If curr node lies in the range, update its
    # left and right nodes and return curr node.
    if l <= root.data <= r:
        root.left = left
        root.right = right
        return root

    # If current node is less than range,
    # then return the updated right subtree.
    elif root.data < l:
        return right

    # Else return the updated left subtree.
    else:
        return left


if __name__ == "__main__":

    # BST
    #          6
    #       /    \
    #     -13     14
    #       \    /  \
    #       -8  13   15
    #         /
    #        7
    root = Node(6)
    root.left = Node(-13)
    root.right = Node(14)
    root.left.right = Node(-8)
    root.right.left = Node(13)
    root.right.right = Node(15)
    root.right.left.left = Node(7)

    l, h = -10, 13
    ans = removekeys(root, l, h)
    levelOrder(ans)
