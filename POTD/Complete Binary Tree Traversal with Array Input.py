# Level-Based Partition and Sort - O(n log n) Time and O(n) Space

def levelSort(arr):
    n = len(arr)
    level = 0
    # Initialize the result list with the first level containing the root node
    res = [[arr[0]]]
    i = 1
    
    # Loop through the array to partition it into levels and sort each level
    while i < n:
        level += 1
        
        # Initialize a temporary list to store the nodes of the current level
        q = []
        
        # Calculate the number of nodes at the current level
        level_num = 2 ** level if(i + 2 ** level) < n else n - i
        
        
        # Append the nodes of the current level to the temporary list
        for j in range(level_num):
            q.append(arr[i + j])
            
        q.sort()
        res.append(q)
        
        # Increment the index to move to the next level
        i += level_num
    
    return res
            

arr = [7, 16, 1, 4, 13]
print(levelSort(arr))
