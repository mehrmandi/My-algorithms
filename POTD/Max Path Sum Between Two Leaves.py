# Given the root of a binary tree, where each node contains an integer value, find the maximum possible path sum between any two leaf nodes. If the tree has fewer than two leaf nodes, return -1.


# Postorder DFS - O(n) Time and O(h) Space


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def dfsUtil(node, res):
    if not node.left and not node.right:
        return node.data
    
    left = dfsUtil(node.left, res) if node.left else float("-inf")
    right = dfsUtil(node.right, res) if node.right else float("-inf")
    
    if node.right and node.left:
        res[0] = max(res[0], left + node.data + right)
        

    return node.data + max(left, right)

def maxPathSum(root):
    if not root:
        return -1
    
    res = [float("-inf")]
    
    dfsUtil(root, res)
    
    if res == [float("-inf")]:
        return -1
    
    return res[0]

root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(9)
root.left.left.left = Node(2)
root.left.left.right = Node(-3)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)

print(maxPathSum(root))

