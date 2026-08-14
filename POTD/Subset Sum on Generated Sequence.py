# There are n children standing in a queue, each assigned a number arr[i]. The teacher writes s on a paper and gives it to the first child. Each child writes the sum of all numbers already on the paper and arr[i], then passes it to the next child.

# Return true if x can be formed by adding some of the numbers written on the paper, else return false.


# Using Greedy - O(n) Time and O(n) Space

def isPossible(arr, s, x):
    n = len(arr)
    # Generate the sequence written on the paper.
    seq = [s]

    prefSum = s

    for val in arr:
        cur = prefSum + val
        seq.append(cur)
        prefSum += cur

    # Greedily subtract the largest possible values.
    target = x

    for i in range(n, -1, -1):
        if seq[i] <= target:
            target -= seq[i]

    return target == 0
    

arr = [7, 9, 6, 5, 8, 7, 6, 6, 7, 8]
s = 5
x = 10860

print(isPossible(arr, s, x))
