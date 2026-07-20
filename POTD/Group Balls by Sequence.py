from collections import Counter
import heapq


def can_form_groups(arr, k):
    if len(arr) % k != 0:
        return False  # Cannot evenly divide the array into groups of k

    freq = Counter(arr)
    print(freq)
    min_heap = list(freq.keys())
    heapq.heapify(min_heap)  # Always access the smallest number efficiently
    print(min_heap)

    while min_heap:
        first = min_heap[0]
        # Try to form a group starting from 'first'
        for num in range(first, first + k):
            if freq[num] == 0:
                return False  # Required number is missing
            freq[num] -= 1
            if freq[num] == 0:
                if num != min_heap[0]:
                    return False  # Ensure the heap is consistent
                heapq.heappop(min_heap)

    return True
       
        
            
arr = [1, 2, 2, 3, 3, 4, 4, 4, 5]
k = 3
print(can_form_groups(arr, k))
