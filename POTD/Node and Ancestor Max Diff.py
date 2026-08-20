# Given the root of a binary tree, find the maximum value of A - B, where A is an ancestor of node B


# Postorder Traversal with Minimum Subtree Value - O(n) Time and O(h) Space


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Returns the maximum difference between a node and its ancestor in the subtree with the current node as an endpoint.
def findMaxDiffRec(root, res):
    if not root:
        return float("inf")
    
    if not root.left and not root.right:
        return root.data

    # Calculate minimum value in left and right subtrees
    sub_res = min(findMaxDiffRec(root.left, res), findMaxDiffRec(root.right, res))
    
    # Update 'res' with the maximum difference between the current node and its ancestor
    res[0] = max(res[0], root.data -sub_res)
    
    # Return the minimum value in the subtree rooted at the current node
    return min(sub_res, root.data)
    

def maxDiff(root):
    res = [float("-inf")]
    
    # Compute maximum difference and store it in 'res'
    findMaxDiffRec(root, res)

    return res[0]

  # Representation of input binary tree:
    #            10
    #           /  \
    #          2    10
    #         / \     \
    #        20  1    -25
    #          \       /  \
    #           8     3     4



root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
root.left.left.right = Node(8)


print(maxDiff(root))