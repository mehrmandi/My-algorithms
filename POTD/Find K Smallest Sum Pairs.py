import heapq

def kSmallestPair(arr1, arr2, k):
    ans = []

    # Min-heap to keep track of current smallest sum and indices
    pq = []
    my_set = set()

    # Push initial pair (arr1[0] + arr2[0]) with indices (0,0)
    heapq.heappush(pq, (arr1[0] + arr2[0], 0, 0))
    my_set.add((0, 0))

    flag = 1
    count = 0
    while count < k and flag != 0:
        temp = heapq.heappop(pq)
        sum_val, i, j = temp

        # Add the current smallest pair to the answer
        ans.append([arr1[i], arr2[j]])

        flag = 0
        # Push next element in arr1 (if not already used)
        if i + 1 < len(arr1):
            temp1 = (i + 1, j)
            if temp1 not in my_set:
                heapq.heappush(pq, (arr1[i + 1] + arr2[j], i + 1, j))
                my_set.add(temp1)
            flag = 1

        # Push next element in arr2 (if not already used)
        if j + 1 < len(arr2):
            temp1 = (i, j + 1)
            if temp1 not in my_set:
                heapq.heappush(pq, (arr1[i] + arr2[j + 1], i, j + 1))
                my_set.add(temp1)
            flag = 1

        count += 1

    return ans
                
                
    



arr1 = [1, 7, 11]
arr2 = [2, 4, 6]
k = 3
print(kSmallestPair(arr1, arr2, k))
