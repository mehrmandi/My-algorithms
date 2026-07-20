class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def helper(root, k, closest):
    if not root:
        return closest
    
    if root.data == k:
        return k
    
    if root.data > k:
        helper(root.left, k, closest)
        
    if root.data < k:
        closest[0] = root.data
        helper(root.right, k, closest)
        
    return closest
    
def closestNeighbour(root, k):
    closest = [-1]
    
    return helper(root, k, closest)
    
    
# root = [10, 7, 15, 2, 8, 11, 16]
k = 4

root = Node(5)
root.left = Node(2)
root.right = Node(12)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(21)
root.right.left = Node(9)
root.right.right.right = Node(25)
root.right.right.left = Node(19)


print(closestNeighbour(root, k))
    