import heapq


def smallestRange(arr):
    k = len(arr)  # Number of lists
    min_heap = []
    max_value = float('-inf')  # To track the max value in the heap
    start, end = float('-inf'), float('inf')  # Final range
    pointers = [0] * k  # Keep track of indices in each row

    # Initialize the heap with the first element from each row
    for i in range(k):
        heapq.heappush(min_heap, (arr[i][0], i))
        max_value = max(max_value, arr[i][0])

    while min_heap:
        min_value, row = heapq.heappop(min_heap)
        print(max_value, min_value, row)

        # Update the range if we found a smaller one
        if max_value - min_value < end - start:
            start, end = min_value, max_value

        pointers[row] += 1  # Move forward in the row

        # If we've exhausted a row, break (since we can't cover all lists anymore)
        if pointers[row] == len(arr[row]):
            break

        # Add the next element from the same row into the heap
        next_value = arr[row][pointers[row]]
        heapq.heappush(min_heap, (next_value, row))
        max_value = max(max_value, next_value)

    return [start, end]

        
        
arr = [
    [16, 20, 34, 35, 100],
    [36, 51, 54, 70, 88],
    [3, 38, 63, 88, 90],
    [5, 6, 11, 12, 61],
    [4, 17, 30, 58, 93],
    [6, 22, 23, 44, 80]
]
print(smallestRange(arr))
