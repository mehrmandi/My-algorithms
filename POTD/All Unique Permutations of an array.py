def backtrack(arr, visited, curr, result):

    # If current permutation is complete, add it to the result
    if len(curr) == len(arr):
        result.append(curr[:])
        return

    # Iterate through the array to build permutations
    for i in range(len(arr)):

        # Skip already visited elements or duplicates
        if visited[i] or (i > 0 and arr[i] == arr[i - 1] and not visited[i - 1]):
            continue

        # Choose arr[i] for the current permutation
        visited[i] = True
        curr.append(arr[i])

        # Recursively build the next part of the permutation
        backtrack(arr, visited, curr, result)

        # Backtrack
        curr.pop()
        visited[i] = False

# Function to return all unique permutations


def uniquePerms(arr):
    # Sort the array to handle duplicates
    arr.sort()
    result = []
    visited = [False] * len(arr)

    # Start the backtracking process
    backtrack(arr, visited, [], result)

    return result


if __name__ == "__main__":
    arr = [1, 3, 3]
    permutations = uniquePerms(arr)

    for perm in permutations:
        print(" ".join(map(str, perm)))
