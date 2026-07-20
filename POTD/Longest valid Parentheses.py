def maxLength(s):
    st = []
    n = len(s)

    st.append(-1)
    max_len = 0

    for i in range(n):
        if s[i] == "(":
            st.append(i)
            print(st)
        else:
            st.pop()

            if not st:
                st.append(i)
                print("other", st)

            else:
                max_len = max(max_len, i - st[-1])


    return max_len

s = "()((()"
print(maxLength(s))



# (((((((()(()()))()(()())))
# ()((()(((((((()(()()))()(()())))