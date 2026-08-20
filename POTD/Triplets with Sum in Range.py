# Given an array arr[] of n distinct integers and a range from l to r, the task is to count the number of triplets having a sum in the range[l, r].

# Using Sorting + Two Pointers – O(n²) Time and O(1) Space

def countTriplets(arr: list[int], l: int, r: int) -> int:
    n = len(arr)
    arr.sort()
    res = 0
    
    # Count triplets with sum less than or equal to x
    def countLowerTriplets(arr, x):
        count = 0
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            # Use two pointers to find pairs with sum less than or equal to x - arr[i]
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                
                if curr_sum <= x:
                    count += (right - left)
                    left += 1
                    
                else:
                    right -= 1
                    
        return count
    
    # Count triplets with sum in the range [l, r]
    return countLowerTriplets(arr, r) - countLowerTriplets(arr, l - 1)
                    
        
    


arr = [5, 1, 4, 3, 2]
l = 2
r = 7
print(countTriplets(arr, l, r))
    