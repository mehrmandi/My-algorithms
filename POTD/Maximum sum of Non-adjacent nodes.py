class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Python program to find the maximum sum in a Binary Tree
# such that no two nodes are adjacent.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Helper function to find the maximum sum
def maxSumHelper(root):
    if root is None:
        return (0, 0)

    # Recursively get the maximum sum for left
    # and right subtrees
    leftSum = maxSumHelper(root.left)
    rightSum = maxSumHelper(root.right)
    print(leftSum, rightSum, root.data)

    # This node is included (children are not included)
    include = leftSum[1] + rightSum[1] + root.data

    # This node is excluded (children may be included)
    exclude = max(leftSum[0], leftSum[1]) + max(rightSum[0], rightSum[1])

    return (include, exclude)


# Function to get the maximum sum with
# the given constraints
def getMaxSum(root):
    result = maxSumHelper(root)
    return max(result[0], result[1])


if __name__ == "__main__":

    # Creating a binary tree with the following structure:
    #          1
    #         / \
    #        2   3
    #       /   / \
    #      1   4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.left.left = Node(1)
    print(getMaxSum(root))



