# def hIndex(citations):
#     citations.sort(reverse=True)
#     h_index = 0
#     for i, c in enumerate(citations):
#         if c >= i + 1:
#             h_index = i + 1
#         else:
#             break
#     return h_index



# citations = [8, 12, 10, 12, 9, 12]
# print(hIndex(citations))

# [Expected Approach] Using Counting Sort - O(n) Time and O(n) Space----------------------------------------

def hIndex(citations):
    n = len(citations)
    freq = [0] * (n + 1)

    # count the frequency of citations
    for citation in citations:
        if citation >= n:
            freq[n] += 1
        else:
            freq[citation] += 1

    idx = n

    # variable to keep track of the count of papers
    # having at least idx citations
    s = freq[n]
    while s < idx:
        idx -= 1
        s += freq[idx]

    # return the largest index for which the count of
    # papers with at least idx citations becomes >= idx
    return idx


if __name__ == '__main__':
    citations = [6, 0, 3, 5, 3]
    print(hIndex(citations))
