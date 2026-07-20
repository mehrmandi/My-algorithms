class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def findPaths(root, path=[], paths=[]):
    if root is None:
        return

    path.append(root.data)

    # If it's a leaf node, store the path
    if not root.left and not root.right:
        paths.append(list(path))
    else:
        findPaths(root.left, path, paths) 
        findPaths(root.right, path, paths)

    path.pop()  # Backtrack
    
    
def rootToLeaf(root):
    paths = []
    findPaths(root, [], paths)
    return paths
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(rootToLeaf(root))


