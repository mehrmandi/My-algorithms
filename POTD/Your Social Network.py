# Geek is creating a social networking site called Geeksbook with n users numbered from 1 to n. Each user i(2 ≤ i ≤ n) has exactly one friend, and that friend must have a smaller user number than i. User 1 has no friend. The friends of users 2 to n are given in an array arr[] of size n - 1, where:

# arr[0] is the friend of user 2.
# arr[1] is the friend of user 3.
# ...
# arr[i - 2] is the friend of user i.
# The relationship is one-way. A user can reach another user by repeatedly following their friend's link. For every user i from 2 to n, find all users j(1 ≤ j < i) that can be reached from i. For every reachable pair(i, j), create an array[i, j, k] where:

# i is the starting user.
# j is the reachable user.
# k is the number of links that must be followed to reach j from i.
# The result should contain these arrays in the following order:

# Process users i from 2 to n.
# For each user i, consider users j from 1 to i - 1 in increasing order.
# Include[i, j, k] only if j is reachable from i.

# Return a 2D array containing information about all reachable pairs.

# Using Dynamic Programming - O(n ^ 2) Time and O(n ^ 2) Space

def socialNetwork(arr):
    n = len(arr) + 1

    # dist[i][j] stores the number of links required
    # to reach user j from user i.
    dist = [[0] * (n + 1) for _ in range(n + 1)]

    # Store all reachable connections.
    ans = []

    # Process users from 2 to n.
    for i in range(2, n + 1):

        # User i has a direct link to arr[i - 2].
        friend_user = arr[i - 2]

        # Direct connection requires 1 link.
        dist[i][friend_user] = 1

        # Reuse the connections already computed for friend_user.
        for j in range(1, i):
            if dist[friend_user][j] > 0:

                # Add one link from i to friend_user.
                dist[i][j] = dist[friend_user][j] + 1

    # Generate the answer in the required order.
    for i in range(2, n + 1):

        # Consider users j in increasing order.
        for j in range(1, i):
            if dist[i][j] > 0:

                # Store {starting user, reachable user, distance}.
                ans.append([i, j, dist[i][j]])

    return ans
    


arr = [1, 2]
print(socialNetwork(arr))
