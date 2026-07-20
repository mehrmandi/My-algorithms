class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def inOrderTraversal(root, n):
    if not root:
        return
    inOrderTraversal(root.left, n)
    n[0] += 1
    inOrderTraversal(root.right, n)
    

def kthSmallest(root, k):
    count = 0
    curr = root

    while curr is not None:
        if curr.left is None:
            count += 1
            if count == k:
                return curr.data
            curr = curr.right
        else:
            # Find the inorder predecessor of curr
            prev = curr.left
            while prev.right is not None and prev.right != curr:
                prev = prev.right

            # Make curr the right child of its inorder predecessor
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                count += 1
                if count == k:
                    return curr.data

                # Revert the changes made in the tree structure
                prev.right = None
                curr = curr.right
    return -1


def findMedian(root):
    n = [0]
    inOrderTraversal(root, n)
    
    k = 0
    if n[0] % 2 == 0:
        k = n[0] / 2
    
    else:
        k = (n[0] + 1) / 2
        
    return kthSmallest(root, k)


root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(1)
# root.left.right = Node(12)
# root.left.right.left = Node(10)
# root.left.right.right = Node(14)

print(findMedian(root))
        
        
    
    
    
    
    
