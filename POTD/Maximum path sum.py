class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Returns the maximum path
# sum in the subtree with the current node as an endpoint.


def findMaxSumRec(root, res):

    if root is None:
        return 0
    
    print(root.data, res)

    # Calculate maximum path sums for left and right subtrees
    l = max(0, findMaxSumRec(root.left, res))
    print("l", root.data, l, res)
    r = max(0, findMaxSumRec(root.right, res))
    
    print("vasast", l, r, res)

    # Update 'res' with the maximum path
    # sum passing through the current node
    res[0] = max(res[0], l + r + root.data)

    print("res return", root.data, l, r, root.data + max(l, r))
    return root.data + max(l, r)




# Returns maximum path sum in tree with given root


def findMaxSum(root):
    res = [root.data]

    # Compute maximum path sum and store it in 'res'
    findMaxSumRec(root, res)

    return res[0]


if __name__ == "__main__":

    # Representation of input binary tree:
    #            10
    #           /  \
    #          2    10
    #         / \     \
    #        20  1    -25
    #                 /  \
    #                3     4
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    root.left.left.right = Node(8)

    print(findMaxSum(root))
