# Function to decode given encoded string without using stack.

def decodedString(s):
    res = ""

    for i in range(len(s)):

        if s[i] != ']':
            res += s[i]

        else:

            temp = ""
            while res and res[-1] != '[':
                temp = res[-1] + temp
                res = res[:-1]

            res = res[:-1]

            num = ""
            while res and res[-1].isdigit():
                num = res[-1] + num
                res = res[:-1]
            p = int(num)

            res += temp * p

    return res


s = "3[a3[b]2[ab]]"
print(decodedString(s))


# abbbababbbababbbab
# abbbabababbbabababbbabab

