class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def countPathsUtil(node, k, currSum, prefSums):

    if node is None:
        return 0

    pathCount = 0
    currSum += node.data

    # Pathsum from root to current node is equal to k
    if currSum == k:
        pathCount += 1


    pathCount += prefSums.get(currSum - k, 0)

    # Add the current sum into the hashmap
    prefSums[currSum] = prefSums.get(currSum, 0) + 1

    pathCount += countPathsUtil(node.left, k, currSum, prefSums)
    pathCount += countPathsUtil(node.right, k, currSum, prefSums)

    # Remove the current sum from the hashmap
    prefSums[currSum] -= 1

    return pathCount

# Function to find the paths in the tree which have their sum equal to K
def countAllPaths(root, k):
    prefSums = {}
    return countPathsUtil(root, k, 0, prefSums)


root = Node(8)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.right = Node(2)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right.right = Node(1)

k = 7
print(countAllPaths(root, k))
