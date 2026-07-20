# from bisect import bisect_left

# def insertInterval(intervals, newInterval):
#     n = len(intervals)
#     starts = []
#     ends = []
#     res = []
    
#     for interval in intervals:
#         starts.append(interval[0])
#         ends.append(interval[1])
        
#     starts_index = bisect_left(starts, newInterval[0])
#     ends_index = bisect_left(ends, newInterval[1])
    
#     starts.insert(starts_index, newInterval[0])
#     ends.insert(ends_index, newInterval[1])
    
    
#     prev_start = starts[0]
#     prev_end = ends[0]
    
#     for i in range(1, n + 1):
#         start = starts[i]
#         end = ends[i]
        
#         if prev_start <= start <= prev_end:
#             prev_end = end
        
#         else:
#             res.append([prev_start, prev_end])
#             prev_start = start
#             prev_end = end
        
#     res.append([prev_start, prev_end])
#     return res
            

# intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
# newInterval = [5, 6]
# print(insertInterval(intervals, newInterval))


# [Expected Approach] Contiguous Interval Merging - O(n) Time and O(n) Space---------------------------------------
def insertInterval(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before the new interval
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # Merge all overlapping intervals with the new interval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    res.append(newInterval)

    # Add all the remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res


if __name__ == "__main__":
    intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
    newInterval = [5, 6]

    print(insertInterval(intervals, newInterval))
    
