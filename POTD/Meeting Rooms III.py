import heapq


def mostBooked(n, meetings):
    # Sort meetings by start time
    meetings.sort()

    # Min-heap for available rooms
    available_rooms = list(range(n))
    heapq.heapify(available_rooms)

    # Min-heap for ongoing meetings (end_time, room_number)
    occupied_rooms = []

    # Room usage count
    room_count = [0] * n

    for start, end in meetings:
        # Free up rooms that are now available
        while occupied_rooms and occupied_rooms[0][0] <= start:
            heapq.heappush(available_rooms, heapq.heappop(occupied_rooms)[1])

        if available_rooms:
            # Assign meeting to the smallest available room
            room = heapq.heappop(available_rooms)
        else:
            # Delay the meeting until the earliest room becomes available
            end_time, room = heapq.heappop(occupied_rooms)
            end = end_time + (end - start)

        # Record room usage and add to occupied list
        room_count[room] += 1
        heapq.heappush(occupied_rooms, (end, room))

    # Find the room with the maximum number of meetings
    max_meetings = max(room_count)
    return min(i for i in range(n) if room_count[i] == max_meetings)


# Example
n = 4
meetings = [[0, 8], [1, 4], [3, 4], [2, 3]]
print(mostBooked(n, meetings))  # Output: 0


# [Expected Approach] Using Two priority queue - O(m*log m+m*log n) Time and O(n) Space

# def mostBooked(n, meetings):

# 	# Count of meetings per room
#     cnt = [0] * n

#     # Min-heap for occupied rooms: (end time, room number)
#     occ = []

#     # Min-heap for available rooms: room numbers
#     avail = list(range(n))

#     # Sort meetings by start time
#     meetings.sort()

#     for s, e in meetings:
#         # Release rooms that have become available by time s
#         while occ and occ[0][0] <= s:
#             _, r = heapq.heappop(occ)
#             heapq.heappush(avail, r)

#         if avail:
#             # Assign to the smallest available room
#             r = heapq.heappop(avail)
#             heapq.heappush(occ, (e, r))
#             cnt[r] += 1
#         else:
#             # All rooms are occupied; assign to the room that becomes free earliest
#             t, r = heapq.heappop(occ)
#             heapq.heappush(occ, (t + (e - s), r))
#             cnt[r] += 1

#     # Find the room with the maximum number of meetings
#     res = max(range(n), key=lambda i: cnt[i])
#     return res


# if __name__ == "__main__":
#     n = 2
#     meetings = [[0, 6], [2, 3], [3, 7], [4, 8], [6, 8]]
#     print(mostBooked(n, meetings))
