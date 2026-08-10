# Given two integer arrays h[] and l[], where h[i] and l[i] denote the number of tasks that can be completed on the i-th day by performing a high-effort task and a low-effort task, respectively. For each day, you may choose exactly one of the following:

# Perform no task.
# Perform a low-effort task.
# Perform a high-effort task, which can only be performed on the first day or if no task was performed on the previous day.
# Return the maximum total number of tasks that can be completed over all days.


#  Using Space Optimized Dynamic Programming - O(n) Time and O(1) Space


def maxTask(h: list[int], l: list[int]) -> int:
    n = len(h)
    if n == 0:
        return 0

    # prev2 -> dp[i-2], prev1 -> dp[i-1]
    prev2 = 0

    # day 0: choose best of h or l
    prev1 = max(h[0], l[0])

    # if only one day
    if n == 1:
        return prev1

    # day 1: either take h, or l + prev best
    curr = max(h[1], l[1] + prev1)

    prev2 = prev1
    prev1 = curr

    # process remaining days
    for i in range(2, n):

        # option 1: take l today + best till yesterday
        # option 2: take h today + best till day before yesterday
        curr = max(l[i] + prev1, h[i] + prev2)

        prev2 = prev1
        prev1 = curr

    return prev1
        
            
            
            
            


h = [3, 6, 8, 7, 6]
l = [1, 5, 4, 5, 3]
