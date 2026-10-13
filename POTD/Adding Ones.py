# Consider an array arr[] of size n, initially containing all zeros. You are also given an array updates[] of k positive integers. For each value j in updates[], add 1 to every element arr[i] whose index satisfies i ≥ j. The indices in updates[] are 1-based.

# Perform all the updates and modify arr[] accordingly.

# Frequency Counting + Prefix Sum - O(n + k) Time and O(n) Space

def update(n: int, updates: list[int]) -> list[int]:
    arr = [0] * n

    # Count the number of updates starting at each position.
    for j in updates:
        arr[j - 1] += 1

    # Build the final array using prefix sum.
    count = 0

    for i in range(n):
        count += arr[i]
        arr[i] = count

    return arr

n = 2
updates = [1, 1, 1]
print(update(n, updates))
    
    
    
