# Given an integer array files[], where files[i] represents the size of the i-th file, merge all the files into a single file with the minimum total computation cost.

# The cost of merging two files of sizes x and y is x + y. After merging, a new file of size x + y is created, which can be merged further with other files.

# Return the minimum total cost required to merge all the files.


# Greedy using Min Heap - O(n log n) Time and O(n) Space

import heapq

def minComputation(files):
    min_heap = files[:]
    heapq.heapify(min_heap)
    cost = 0
    
    while len(min_heap) > 1:
        first_file = heapq.heappop(min_heap)
        second_file = heapq.heappop(min_heap)
        merged_file = first_file + second_file
        heapq.heappush(min_heap, merged_file)
        cost += merged_file

    return cost
        
    
    
files = [2, 2, 4 , 5, 7, 9, 5 , 12, 15]
print(minComputation(files))
    