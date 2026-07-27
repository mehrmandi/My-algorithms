# Structure of Binary Tree Node

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def constructTreeUtil(pre, preMirror, preIndex, l, h, preMirrorIdx):
    # Base case: If the current index exceeds the length of the preorder array or if the left index is greater than the right index, return None
    if preIndex[0] > len(pre) or l > h:
        return None
    
    # Create a new node with the current value from the preorder array and increment the index
    root = Node(pre[preIndex[0]])
    preIndex[0] += 1
    
    # If there is only one element in the current range, return the node as a leaf node
    if l == h:
        return root
    
    # Find the index of the next preorder element in the preMirror array using the preMirrorIdx mapping
    i = preMirrorIdx[pre[preIndex[0]]]
    
    # If the index is within the current range, recursively construct the left and right subtrees
    if i >= l and i <= h:
        root.left = constructTreeUtil(pre, preMirror, preIndex, i, h, preMirrorIdx)
        root.right = constructTreeUtil(pre, preMirror, preIndex, l + 1, i - 1, preMirrorIdx)
    

    return root

def constructBinaryTree(pre, preMirror):
    # Create a mapping of preMirror values to their indices for quick lookup
    preMirrorIdx = {val: idx for idx, val in enumerate(preMirror)}
    
    # Initialize the preIndex as a list to keep track of the current index in the preorder array
    preIdx = [0]
    return constructTreeUtil(pre, preMirror, preIdx,
                                 0, len(pre) - 1, preMirrorIdx)
    
    
def preOrder(node, res):
    if not node:
        return

    # Visit the current node first
    res.append(node.data)

    # Traverse the left subtree
    preOrder(node.left, res)

    # Traverse the right subtree
    preOrder(node.right, res)

    

    

pre = [1, 2, 4, 5, 3, 6, 7]
preMirror = [1, 3, 7, 6, 2, 5, 4]
root = constructBinaryTree(pre, preMirror)
res = []
preOrder(root, res)
print(res)