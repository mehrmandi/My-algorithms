# Given the roots r1 and r2 of two Binary Search Trees (BST), find all nodes that are present in both trees i.e. the intersection nodes of the two BSTs.

# Return the common node values in sorted order.

# Using Simultaneous Inorder Traversal - O(n + m) Time and O(h1 + h2) Space


#Structure of a Binary Search Tree node


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
        

def findCommon(r1, r2):
    s1 = []
    s2 = []
    res = []
    
    while True:
        while r1:
            s1.append(r1)
            r1 = r1.left
            
        while r2:
            s2.append(r2)
            r2 = r2.left
            
        if len(s1) == 0 or len(s2) == 0:
            break
        
        curr1 = s1[-1]
        curr2 = s2[-1]
        
        if curr1.data == curr2.data:
            res.append(curr1.data)
            s1.pop()
            s2.pop()
            
            r1 = curr1.right
            r2 = curr2.right
            
        elif curr1.data < curr2.data:
            s1.pop()
            r1 = curr1.right
            r2 = None
            
        else:
            s2.pop()
            r2 = curr2.right
            r1 = None
            
    return res
    
            
    

root1 = Node(5)
root1.left = Node(1)
root1.right = Node(10)
root1.left.left = Node(0)
root1.left.right = Node(4)
root1.right.left = Node(7)
root1.right.left.right = Node(9)


root2 = Node(10)
root2.left = Node(7)
root2.right = Node(20)
root2.left.left = Node(4)
root2.left.right = Node(9)

print(findCommon(root1, root2))



    
        