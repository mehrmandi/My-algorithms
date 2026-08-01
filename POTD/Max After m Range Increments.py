# Given three arrays a[], b[], and k[], representing m range increment operations on an array arr[] of size n, where all elements of arr[] are initially 0.

# Increment(a[i], b[i], k[i]) adds k[i] to each element arr[j] such that a[i] ≤ j ≤ b[i](mainly indexes in range from a[i] to b[i])
# After performing all the given operations, find the maximum value present in the array.

# Difference Array Technique - O(m + n) Time and O(n) Space

def findMax(n, a, b, k):
    # Create a difference array of size n + 1
    sub_arr = [0] * (n + 1)
    
    # Apply the range increment operations using the difference array technique
    for i in range(len(a)):
        # Increment the start index by k[i]
        sub_arr[a[i]] += k[i]
        
        # Decrement the index after the end index by k[i] to mark the end of the increment
        if b[i] < n:
            sub_arr[b[i] + 1] -= k[i]
    
    # Calculate the prefix sum to get the final values in the original array        
    sum = 0
    res = float('-inf')
    for i in range(n):
        sum += sub_arr[i]
        res = max(res, sum)
    return res
         

n = 4
a = [1, 0, 3]
b = [2, 0, 3]
k = [603, 286, 882]
print(findMax(n, a, b, k))
