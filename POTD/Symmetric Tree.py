class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
        
def isSymmetric(right, left):
    if not right and not left:
        return True
    if right and left and right.data == left.data:
        return isSymmetric(right.right, left.left) and isSymmetric(right.left, left.right)
    
    return False
   
def symmetricTree(root):
    if not root.left and not root.right:
        return True
    if root.left and root.right:
        return isSymmetric(root.right, root.left)
    else:
        return False


   
root = Node(1)
# root.left = Node(2)
# root.right = Node(2)
# root.right.right = Node(3)
# root.right.left = Node(4)
# root.left.left = Node(3)
# root.left.right = Node(3)
print(symmetricTree(root))
