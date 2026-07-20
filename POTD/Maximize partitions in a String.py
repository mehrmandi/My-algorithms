def stringPartitioning(s):
    n = len(s)
    partition = 0
    flag = False
    part = []

    for i in range(n):
        new = s[i + 1:]
        if s[i] in new:
            part.append(s[i])
        else:
            set_part = list(set(part))
            for j in set_part:
                if j in new:

                    flag = True
                    break
            if not flag:
                partition += 1
        flag = False

    return partition


s = "acbbcc"
print(stringPartitioning(s))



