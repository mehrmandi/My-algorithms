import heapq

# Function to find the kth smallest array element
def kthSmallest(arr, K):
    # Create a max heap (priority queue)
    max_heap = []

    # Iterate through the array elements
    for num in arr:
        # Push the negative of the current element onto the max heap
        heapq.heappush(max_heap, -num)

        print("max_heap", max_heap)

        # If the size of the max heap exceeds K, remove the largest element
        if len(max_heap) > K:
            heapq.heappop(max_heap)
            print("second", max_heap)


    print("last", max_heap)
    # Return the Kth smallest element (top of the max heap, negated)
    return -max_heap[0]

# Driver's code:
if __name__ == "__main__":
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    K = 4

    # Function call
    print("Kth Smallest Element is:", kthSmallest(arr, K))