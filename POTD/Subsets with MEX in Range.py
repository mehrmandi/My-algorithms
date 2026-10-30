# Given an array arr[] of integers and a range[l, r], count the number of subsets whose Minimum Excluded(MEX) value lies within the given range, inclusive.

# Minimum Excluded (or MEX) of a subset is the smallest non-negative integer that is not present in the subset.
# An empty subset has Minimum Excluded as zero.
# Since the answer can be very large, return the answer modulo 109 + 7.

# Combinatorics - O(n + r) Time and O(n) Space


def cntSubsets(arr, l, r):
    M = 1000000007
    n = len(arr)

    mp = {}
    for num in arr:
        mp[num] = mp.get(num, 0) + 1

    # Precompute powers of 2 modulo M.
    power = [1] * (n + 1)
    for i in range(1, n + 1):
        power[i] = (power[i - 1] * 2) % M

    res = 0
    cur = 1
    seen = 0

    # Ensure every value smaller than l is present.
    for i in range(l):
        freq = mp.get(i, 0)

        if freq == 0:
            return 0

        seen += freq
        cur = (cur * (power[freq] - 1 + M)) % M

    # Count subsets for each possible MEX.
    for i in range(l, r + 1):
        freq = mp.get(i, 0)

        here = (cur * power[n - seen - freq]) % M
        res = (res + here) % M

        # No larger MEX is possible if i is absent.
        if freq == 0:
            return res

        seen += freq
        cur = (cur * (power[freq] - 1 + M)) % M

    return res


# Driver Code
if __name__ == "__main__":
    arr = [2, 0, 1, 0]
    l, r = 1, 2

    print(cntSubsets(arr, l, r))
        
       
arr = [2, 0, 1, 1, 3, 4, 5, 3, 4, 5, 5, 5, 5, 6]

l = 3
r = 5
print(cntSubsets(arr, l, r))
    
    