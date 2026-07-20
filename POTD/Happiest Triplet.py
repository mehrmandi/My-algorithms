def smallestDiff(a, b, c):

    # Sort three arrays
    a.sort()
    b.sort()
    c.sort()

    # Traverse three arrays from beginning
    i = j = k = 0
    diff = float('inf')
    x = y = z = 0  # Store result
    while i < len(a) and j < len(b) and k < len(c):
        lo = min(a[i], b[j], c[k])
        hi = max(a[i], b[j], c[k])

        if diff > hi - lo:
            diff = hi - lo
            x = hi
            y = a[i] + b[j] + c[k] - (hi + lo)
            z = lo

        if a[i] == lo:
            i += 1
        elif b[j] == lo:
            j += 1
        else:
            k += 1

    return [x, y, z]


a = [15, 12, 18, 9] 
b = [10, 17, 13, 8] 
c = [14, 16, 11, 5]
print(smallestDiff(a, b, c))
