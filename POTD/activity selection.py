# def activitySelect(start, finish):
#     ans = 0
#
#     # to store the activities
#     arr = []
#
#     for i in range(len(start)):
#         arr.append((finish[i], start[i]))
#
#     # sort the activities based on finish time
#     arr.sort()
#
#     # to store the end time of last activity
#     finishtime = -1
#
#     for i in range(len(arr)):
#         activity = arr[i]
#         if activity[1] > finishtime:
#             finishtime = activity[0]
#             ans += 1
#
#     return ans


# ----------------------------------------------------------------------


import heapq

# Function to solve the activity selection problem


def activitySelection(start, finish):

    # to store results.
    ans = 0

    # Minimum Priority Queue to sort activities in
    # ascending order of finishing time (end[i]).
    p = []
    for i in range(len(start)):
        heapq.heappush(p, (finish[i], start[i]))

    # to store the end time of last activity
    finishtime = -1

    while p:
        activity = heapq.heappop(p)
        if activity[1] > finishtime:
            finishtime = activity[0]
            ans += 1

    return ans


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
print(activitySelection(start, finish))


