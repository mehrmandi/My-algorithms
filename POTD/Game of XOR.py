# Given an integer array arr[], find the XOR of the XOR values of all possible non-empty subarrays of the array.

# Subarray Contribution and XOR Property - O(n) Time and O(1) Space

def subarrayXor(arr):
    n = len(arr)
    res = 0
   
    for i in range(n):
        # Check if (i+1) and (n-i) are both odd
        if ((n - i)*(i - 1)) % 2 == 1:
            
            # Include element in final XOR
            res = res ^ arr[i]
        
    return res
        
    
arr = [3, 9, 1, 2, 6]
print(subarrayXor(arr))