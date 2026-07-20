import heapq

def jobSequencing(deadline, profit):
    # code here
    n = len(deadline)
    ans = [0, 0]

    jobs = [(deadline[i], profit[i]) for i in range(n)]

    jobs.sort()

    pq = []

    for job in jobs:

        if job[0] > len(pq):
            heapq.heappush(pq, job[1])

        elif pq and pq[0] < job[1]:
            heapq.heappop(pq)
            heapq.heappush(pq, job[1])

    while pq:
        ans[1] += heapq.heappop(pq)
        ans[0] += 1

    return ans

id = [1, 2, 3, 4]
deadline = [11, 2, 5, 8, 11, 10, 1, 6, 3, 8, 10]
profit = [321, 62, 456, 394, 424, 22, 393, 87, 118, 384, 83]
print(jobSequencing(deadline, profit))


# 11 2 5 8 11 10 1 6 3 8 10
# 321 62 456 394 424 22 393 87 118 384 83