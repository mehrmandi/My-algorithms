# Using Stack - O(n) Time and O(n) Space

def canRepresentBST(arr):
    n = len(arr)
    # stack for storing the ancestors
    st = []
    
    # Initialize current root as minimum possible value
    root = float('-inf')
    
    for i in range(n):
        # If we find a node who is on the right side and smaller than root, return False
        if arr[i] < root:
            return False
        # If arr[i] is in right subtree of stack top, keep removing items smaller than arr[i] and make the last removed item as new root
        while st and st[-1] < arr[i]:
            root = st.pop()
        
        # Push the current node to stack    
        st.append(arr[i])
        
    return True


        

arr = [2, 4, 1]
print(canRepresentBST(arr))
