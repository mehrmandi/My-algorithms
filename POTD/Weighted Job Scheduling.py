# import bisect


# def jobScheduling(jobs):
#     # Sort jobs by end time
#     jobs.sort(key=lambda x: x[1])

#     # Extract start, end, and profit lists
#     start_times = [job[0] for job in jobs]
#     end_times = [job[1] for job in jobs]
#     profits = [job[2] for job in jobs]

#     # DP array: (end_time, max_profit)
#     dp = [(0, 0)]  # Base case: no job, zero profit

#     for i in range(len(jobs)):
#         # Binary search to find the last job that ends <= current job's start
#         idx = bisect.bisect_right(dp, (start_times[i], float('inf'))) - 1
#         print(dp, idx, i, start_times[i])
#         curr_profit = dp[idx][1] + profits[i]

#         # Only add if it's better than previous max
#         if curr_profit > dp[-1][1]:
#             dp.append((end_times[i], curr_profit))

#     return dp[-1][1]


# jobs = [[3, 5, 20],
#         [6, 19, 100],
#         [1, 2, 50],
#         [2, 100, 200]]
# print(jobScheduling(jobs))


import heapq


def maxProfit(jobs):

    jobs.sort()

    # Min-heap to store {end time, total profit till now}
    pq = []
    maxProfit = 0

    for start, end, profit in jobs:

        # Remove jobs that end before current job starts
        while pq and pq[0][0] <= start:
            maxProfit = max(maxProfit, heapq.heappop(pq)[1])

        # Push current job with profit + best profit so far
        heapq.heappush(pq, (end, profit + maxProfit))

    # Final maximum profit among all chains
    while pq:
        maxProfit = max(maxProfit, heapq.heappop(pq)[1])

    return maxProfit


if __name__ == "__main__":
    jobs = [
        [1, 2, 50],
        [3, 5, 20],
        [6, 19, 100],
        [2, 100, 200]
    ]

    print(maxProfit(jobs))
