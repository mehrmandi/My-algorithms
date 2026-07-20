# def areRotations(s1, s2):
#     n = len(s1)
#     m = len(s2)
    
#     if n != m :
#         return False
    
#     new_s = s1 + s1
    
#     for i in range(n * 2):
#         if new_s[i:i + n] == s2:
#             return True
        
#     return False


# s1 = "abcd"
# s2 = "acbd"
# print(areRotations(s1, s2))


# constants
mod = 10**9 + 7
base1 = 31
base2 = 37


def add(a, b):
    return (a + b) % mod


def subtract(a, b):
    return (a - b + mod) % mod


def multiply(a, b):
    return (a * b) % mod

# builds prefix hashes and powers


def buildHashes(s):
    n = len(s)
    preHash = [[0, 0] for _ in range(n + 1)]
    power = [[1, 1] for _ in range(n + 1)]

    for i in range(n):
        preHash[i + 1][0] = \
            add(multiply(preHash[i][0], base1), ord(s[i]))
        preHash[i + 1][1] = \
            add(multiply(preHash[i][1], base2), ord(s[i]))

        power[i + 1][0] = multiply(power[i][0], base1)
        power[i + 1][1] = multiply(power[i][1], base2)

    return preHash, power

# returns hash of s[left..right-1]


def getHash(preHash, power, left, right):
    return [
        subtract(preHash[right][b],
                 multiply(preHash[left][b], power[right - left][b]))
        for b in range(2)
    ]

# function to check if s2 is a rotation of s1


def areRotations(s1, s2):
    if len(s1) != len(s2):
        return False

    # concatenate s1 with itself to include
    # all possible rotations
    concat = s1 + s1
    n = len(s1)

    # build rolling hash for the concatenated
    # string and s2
    preHashConcat, powerConcat = buildHashes(concat)
    preHashS2, powerS2 = buildHashes(s2)

    # compute the full hash of s2
    targetHash = getHash(preHashS2, powerS2, 0, n)

    # slide a window of size n over concat
    # and compare hashes
    for i in range(len(concat) - n + 1):
        # get hash of substring concat[i...i+n-1]
        subHash = getHash(preHashConcat, powerConcat, i, i + n)
        if subHash == targetHash:
            return True

    # no matching rotation found
    return False


if __name__ == "__main__":
    s1 = "aab"
    s2 = "aba"
    if areRotations(s1, s2):
        print("true")
    else:
        print("false")

