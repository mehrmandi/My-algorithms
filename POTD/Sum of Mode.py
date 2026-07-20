# from collections import Counter

# def sumOfModes(arr, k):
#     n = len(arr)
#     res = 0
#     if k > n:
#         return res
    
#     for i in range(n - k + 1):
#         sub_arr = arr[i:k + i]
#         sub_arr.sort()
#         dic_counter = Counter(sub_arr)
#         mode = dic_counter.most_common(1)[0][0]
#         res += mode
        
#     return res


# arr = [1, 2, 1, 3, 5]
# k = 2
# print(sumOfModes(arr, k))
    

# def sumOfModes(arr, k):
#     n = len(arr)
#     hash = {item: arr[:k].count(item) for item in set(arr[:k])}
#     max_count = max(hash.values())
#     mode = min([key for key, count in hash.items() if count == max_count])
#     res = mode
    
#     for i in range(1, n - k + 1):
#         hash[arr[i - 1]] -= 1
        
#         if hash[arr[i - 1]] == 0:
#             del hash[arr[i - 1]]
            
#         hash[arr[i + k - 1]] = hash.get(arr[i + k - 1], 0) + 1
        
#         max_count = max(hash.values())
#         mode = min([key for key, count in hash.items() if count == max_count])
        
#         res += mode
    
#     return res
        
        
# arr = [1, 2, 1, 3, 5]
# k = 2
# print(sumOfModes(arr, k))


from collections import defaultdict
import heapq
from typing import List


def sumOfModes(arr, k):
        # code here
        n = len(arr)
        if k <= 0 or k > n:
            return 0

        freq = defaultdict(int)   # value -> count in current window
        # entries: (-count, value); uses lazy deletion
        heap = []

        def push_state(x: int) -> None:
            # Reflect current (freq[x], x) into the heap
            heapq.heappush(heap, (-freq[x], x))

        def add(x: int) -> None:
            freq[x] += 1
            push_state(x)

        def remove(x: int) -> None:
            c = freq[x]
            if c == 1:
                del freq[x]
                # no push needed: absence is represented by not being in freq
            else:
                freq[x] = c - 1
                push_state(x)

        def current_mode() -> int:
            # Pop stale heap tops until it matches live (freq, value)
            while heap:
                negf, x = heap[0]
                f = -negf
                if freq.get(x, 0) == f and f > 0:
                    return x
                heapq.heappop(heap)  # discard stale
            return 0  # shouldn't happen when k>0

        # build first window
        for i in range(k):
            add(arr[i])

        total = current_mode()

        # slide windows
        for i in range(k, n):
            add(arr[i])
            remove(arr[i - k])
            total += current_mode()

        return total
    
