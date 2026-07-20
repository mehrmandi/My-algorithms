# [Expected Approach - 2] Using Iteration - O(n) Time and O(n) Space-----------------------------


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
        

def distCandy(root):
    if not root:
        return 0
    
    res = 0
    balance = {}
    
    q = [(root, 0)]
    
    while q:
        node, state = q.pop()
        
        if not node:
            continue
        
        if state == 0:
            q.append((node, 1))
            q.append((node.left, 0))
            q.append((node.right, 0))
            
            
        else:
            leftBalance = balance.get(node.left, 0)
            rightBalance = balance.get(node.right, 0)
            
            
            res += abs(leftBalance) + abs(rightBalance)
            
            balance[node] = node.data + leftBalance + rightBalance - 1
            
    
    
    return res
    
    
 # Representation of input binary tree:
    #            10
    #           /  \
    #          2    10
    #         / \     \
    #        20  1    -25
    #                 /  \
    #                3     4
root = Node(5)
root.left = Node(0)
root.right = Node(0)
root.right.left = Node(0)
root.right.right = Node(0)


print(distCandy(root))


# [Expected Approach - 1] Using Recursion - O(n) Time and O(h) Space---------------------------------------------------------

# Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# function to find the number of
# moves to distribute all of the candies


def distCandyUtil(root, ans):

    if root is None:
        return 0

    # Traverse left subtree
    l = distCandyUtil(root.left, ans)

    # Traverse right subtree
    r = distCandyUtil(root.right, ans)

    ans[0] += abs(l) + abs(r)

    # Return number of moves to balance
    # current node
    return root.data + l + r - 1

# Function to find the number of moves


def distCandy(root):
    ans = [0]

    distCandyUtil(root, ans)

    return ans[0]


if __name__ == "__main__":

    #  Representation of given Binary Tree
    #         5
    #        / \
    #       0   0
    #          / \
    #         0   0
    root = Node(5)
    root.left = Node(0)
    root.right = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(0)

    print(distCandy(root))
