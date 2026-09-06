# Given an array arr[] of integers, calculate the sum of bitwise AND for all pairs of elements such that the first index is less than the second index.

# O(32 * n) Time and O(1) Space

def pairAndSum(arr):
    ans = 0

    n = len(arr)

    # Traverse over all bits
    for i in range(32):

        # Count number of elements with i'th bit set
        k = 0
        for j in range(n):
            if (arr[j] & (1 << i)):
                k += 1

        # There are k set bits, means k(k-1)/2 pairs.
        # Every pair adds 2^i to the answer. Therefore,
        # we add "2^i * [k*(k-1)/2]" to the answer.
        ans += (1 << i) * (k * (k - 1) // 2)

    return ans


arr = [5, 10, 15]

print(pairAndSum(arr))
