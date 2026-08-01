# Maximum Element with Set Bit
# Time Complexity: O(n × log(max(arr))) - For each bit position, all n elements may be processed once.
# Auxiliary Space: O(1)

def maxSubsetXOR(arr):
    n = len(arr)
    index = 0

    # Process bits from MSB to LSB.
    for bit in range(31, -1, -1):
        if index >= n:
            break

        max_index = index

        # Find an element having the current bit set.
        for i in range(index, n):
            if (arr[i] & (1 << bit)) and \
               arr[i] > arr[max_index]:
                max_index = i

        # No pivot found for this bit.
        if (arr[max_index] & (1 << bit)) == 0:
            continue

        # Place the pivot at the current index.
        arr[index], arr[max_index] = \
            arr[max_index], arr[index]

        # Eliminate the current bit from all other elements.
        for i in range(n):
            if i != index and \
               (arr[i] & (1 << bit)):
                arr[i] ^= arr[index]

        index += 1

    ans = 0

    for num in arr:
        ans ^= num

    return ans


arr = [2, 4, 5]
print(maxSubsetXOR(arr))
