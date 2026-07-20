# Recursive function to find all valid combinations
def findCombinations(n, k, subVector, res, last):

    # Base case: if exact sum and exact count achieved
    if n == 0 and k == 0:
        res.append(subVector[:])
        return

    # If sum or count becomes negative, backtrack
    if n < 0 or k < 0:
        return

    # Try numbers from 'last' to 9
    for i in range(last, 10):

        # Choose the number
        subVector.append(i)
        findCombinations(n - i, k - 1, subVector, res, i + 1)

        # Backtrack
        subVector.pop()


# Function to generate and print all combinations
def combinationSum(n, k):

    # Check if combination is impossible
    if n < k or n > 9 * k:
        return []

    subVector = []
    res = []

    findCombinations(n, k, subVector, res, 1)
    return res


if __name__ == "__main__":
    n, k = 9, 3
    ans = combinationSum(n, k)
    for comb in ans:
        print(*comb)
