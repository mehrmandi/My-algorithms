from collections import Counter
import heapq

def minValue(s, k):
    freq = Counter(s)
    print(freq)
    max_heap = [-f for f in freq.values()]
    heapq.heapify(max_heap)
    print(max_heap)
    for _ in range(k):
        max_freq = heapq.heappop(max_heap)
        if max_freq < 0:
            max_freq += 1  # Decrease frequency by 1
            heapq.heappush(max_heap, max_freq)
            print("baaaaed", max_heap)

    return sum(f * f for f in max_heap)


s = "aaaabbbbbccc"
k = 6
print(minValue(s, k))
