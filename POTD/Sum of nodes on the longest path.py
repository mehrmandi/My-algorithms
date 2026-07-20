
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def findPaths(root, max_len, max_sum, path=0, sub_sum=0):
    if root is None:
        return

    path += 1
    sub_sum += root.data

    # If it's a leaf node, store the path
    if not root.left and not root.right:
        if path > max_len[0]:
            max_len[0] = path
            max_sum[0] = sub_sum
        if path == max_len[0]:
            if sub_sum > max_sum[0]:
                max_sum[0] = sub_sum
        
    else:
        findPaths(root.left, max_len, max_sum, path, sub_sum)
        findPaths(root.right, max_len, max_sum, path, sub_sum)

    path -= 1  # Backtrack


def sumOfLongRootToLeafPath(root):
    max_sum = [0]
    max_len = [0]
    findPaths(root, max_len, max_sum, 0, 0)
    return max_sum


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(20)
root.left.left.left = Node(1)
print(sumOfLongRootToLeafPath(root))


   
    
    
    
    
    