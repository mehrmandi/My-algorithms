from collections import defaultdict, deque


def find_alien_order(words):
    # Step 1: Build the graph
    adj = defaultdict(set)  # adjacency list
    in_degree = {}  # count of incoming edges for topological sort

    # Initialize in_degree for all unique characters
    for word in words:
        for char in word:
            in_degree[char] = 0

    # Build edges by comparing adjacent words
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        # Check for invalid case: longer word before its prefix
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break

    # Step 2: Topological sort using Kahn’s algorithm
    q = deque([ch for ch in in_degree if in_degree[ch] == 0])
    order = []

    while q:
        ch = q.popleft()
        order.append(ch)
        for neighbor in adj[ch]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    # If we processed all characters, return the order
    if len(order) == len(in_degree):
        return ''.join(order)
    else:
        return ""  # Cycle detected


# Example input
words = ["baa", "abcd", "abca", "cab", "cad"]
print(find_alien_order(words))  # Sample output: "bdac" or similar valid order
