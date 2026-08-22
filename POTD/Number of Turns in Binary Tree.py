# Given root of a binary tree and the values of its two nodes p and q, count turns required to travel from node p to q.

# A turn occurs whenever the direction of movement changes from left to right or right to left while traversing the tree.
# If the path between the two nodes does not involve any turns(i.e., the nodes lie on the same straight path), return -1.
# Note: All node values are distinct.

# Using LCA with Path Tracking - O(n) Time and O(n) Space

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Find Lowest Common Ancestor
def lca(root, n1, n2):

    if not root:
        return None

    if root.data == n1 or root.data == n2:
        return root

    leftLca = lca(root.left, n1, n2)
    rightLca = lca(root.right, n1, n2)

    if leftLca and rightLca:
        return root

    return leftLca if leftLca else rightLca

# Get Directions from LCA to target node
def getDirections(root, target, path):
    if not root:
        return False
    
    if root.data == target:
        return True
    
    path.append('L')
    
    # Check in left subtree 
    if getDirections(root.left, target, path):
        return True
    
    path.pop()
    
    path.append('R')
    
    # Check in right subtree
    if getDirections(root.right, target, path):
        return True
    
    path.pop()
    
    return False

# Count the number of turns in the path
def countTurns(path):
    if len(path) < 2:
        return 0
    
    turns = 0
    
    for i in range(1, len(path)):
        if path[i] != path[i - 1]:
            turns += 1
            
    return turns
    

def numberOfTurns(root, p, q):
    Lca = lca(root, p, q)
    
    if Lca is None:
        return -1
    
    path1 = []
    path2 = []
    
    # Get directions from LCA to p and q
    getDirections(Lca, p, path1)
    getDirections(Lca, q, path2)
    
    if Lca.data == p or Lca.data == q:
        path = path2 if Lca.data == p else path1
        
        turns = countTurns(path)
        
    else:
        turns = countTurns(path1) + countTurns(path2) + 1
        
    return -1 if turns == 0 else turns
    
        
    
    

# def numberOfTurns(root, p, q):


#  Create binary tree:
    # 			   1
    #            /   \
    #           2     3
    #                / \
    #               6   7
    #              /
    #             8

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.right.left.left = Node(8)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.left.left = Node(9)
root.right.left.right = Node(10)

p = 5
q = 10
print(numberOfTurns(root, p, q))
