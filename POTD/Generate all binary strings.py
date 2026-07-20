# def binstr(n):
#     res = []
#     res_len = 2 ** n
    
#     for i in range(res_len):
#         binary_dig = bin(i)[2:]
#         while len(binary_dig) < n:
#             binary_dig = "0" + binary_dig
            
#         res.append(binary_dig)
        
        
#     return res

# n = 3
# print(binstr(n))

def binstr(n):
    res = []
    for i in range(1 << n):

        # build string from bits of i
        s = ''.join('1' if (i >> j) & 1 else '0' for j in reversed(range(n)))
        res.append(s)

    return res


if __name__ == "__main__":
    n = 3
    ans = binstr(n)

    print(" ".join(ans))


