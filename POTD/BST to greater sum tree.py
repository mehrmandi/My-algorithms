# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None
        

# def transformTree(root):
#     sum = 0
#     curr = root
    
#     while curr:
#         if not curr.right:
#             print("not right", sum, curr.data)
#             sum += curr.data
#             curr.data = sum
#             curr = curr.left
#             print("innnnnnnn", sum, curr.data)
            
#         else:
#             print("chap", curr.data)
#             prev = curr.right
#             while prev.left and prev.left != curr:
#                 prev = prev.left
                
#             if not prev.left :
#                 print("not chap", prev.data)
#                 prev.left = curr
#                 curr = curr.right
#                 print(curr.data)
#             else:
#                 print("hast chap", prev.data)
#                 prev.left = None
#                 sum += curr.data
#                 curr.data = sum
#                 curr = curr.left
#                 print("ooooon", sum, curr.data)
                
                
#     return root




     
# root = Node(11)
# root.left = Node(2)
# root.right = Node(29)
# root.left.left = Node(1)
# root.left.right = Node(7)
# root.right.left = Node(15)
# root.right.right = Node(40)
# root.right.right.left = Node(35)


# print(transformTree(root))


from collections import deque

# Node structure


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Calculate Height


def getHeight(root, h):
    if root is None:
        return h - 1
    return max(getHeight(root.left, h + 1), getHeight(root.right, h + 1))

# Print Level Order


def levelOrder(root):
    queue = deque([[root, 0]])
    lastLevel = 0

    # function to get the height of tree
    height = getHeight(root, 0)

    # printing the level order of tree
    while queue:
        node, lvl = queue.popleft()

        if lvl > lastLevel:
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


# Function to update the tree
def updateTree(root, sum):
    if root is None:
        return

    # Traverse the right subtree first (larger values)
    updateTree(root.right, sum)

    # Update the sum and the current node's value
    sum[0] += root.data
    root.data = sum[0] - root.data

    # Traverse the left subtree (smaller values)
    updateTree(root.left, sum)

# Return the updated tree


def transformTree(root):

    # Initialize the cumulative sum
    sum = [0]
    updateTree(root, sum)


if __name__ == "__main__":

    #   Constructing the BST
    #      11
    #     /  \
    #    2    29
    #   / \   / \
    #  1   7 15  40
    #            /
    #           35

    root = Node(11)
    root.left = Node(2)
    root.right = Node(29)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.left = Node(35)

    transformTree(root)
    levelOrder(root)
