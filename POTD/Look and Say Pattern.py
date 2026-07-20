

def countAndSay(n):
    if n == 1:
        return "1"

    curr = "1"

    # Start from the second term, build every term
    # terms using the previous term
    for i in range(2, n + 1):
        nextStr = ""
        cnt = 1

        for j in range(1, len(curr)):

            # If same as previous, then increment
            # count
            if curr[j] == curr[j - 1]:
                cnt += 1

            # If different process the previous
            # character and its count and reset
            # count for the current character
            else:
                nextStr += str(cnt) + curr[j - 1]
                cnt = 1

        nextStr += str(cnt) + curr[-1]
        curr = nextStr

    return curr


# Driver code
if __name__ == "__main__":
    n = 10
    print(countAndSay(n))
    
    
# 1
# 11
# 21
# 1211
# 111221
