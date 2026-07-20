from collections import defaultdict

# Recursive function to generate all subset sums


def genSubset(arr, index, currSum, freq):
    if index == len(arr):
        # store frequency of currSum
        freq[currSum] += 1
        return

    # Include current element
    genSubset(arr, index + 1, currSum + arr[index], freq)

    # Skip current element
    genSubset(arr, index + 1, currSum, freq)

# Function to count subsets whose sum equals k using frequency maps


def countSubset(arr, k):
    n = len(arr)
    mid = n // 2

    # Split array into two halves
    left = arr[:mid]
    right = arr[mid:]

    # Store frequency of all subset sums
    freqLeft = defaultdict(int)
    freqRight = defaultdict(int)
    genSubset(left, 0, 0, freqLeft)
    genSubset(right, 0, 0, freqRight)

    count = 0
    
    # Multiply frequencies of pairs that sum to k
    for sumLeft, fLeft in freqLeft.items():
        target = k - sumLeft
        
        if target in freqRight:
            count += fLeft * freqRight[target]

    return count
    

arr = [4, 2, 3, 1, 2]
k = 4
print(countSubset(arr, k))